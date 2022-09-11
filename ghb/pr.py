#
# Open a GitHub PR from the current branch to master or a specified branch
# Edit the PR message in vim
# Usage: ghb pr [BRANCH]
#
# Example:
# ghb pr # This opens a PR against master
# ghb pr some-branch # This opens the PR against 'some-branch'
#
import json
import os
import subprocess
import sys
import webbrowser

import requests

from .helpers import credentials

URL = "https://api.github.com/repos/%s/pulls"
HEADERS = {"Accept": "application/vnd.github.shadow-cat-preview+json"}


def _run_git_command(command):
    return (
        subprocess.check_output(["git"] + command.split(" ")).decode().strip()
    )


def current_branch_name():
    branch = _run_git_command("symbolic-ref --short HEAD")
    return f"{repo_username()}:{branch}"


def repo_username():
    return repo_with_username().split("/")[0]


def repo_with_username():
    if "@" in origin_url():
        url_parts = filter_empty_string(origin_url().split(":"))
        username_repo = url_parts[-1]
    else:
        url_parts = filter_empty_string(origin_url().split("/"))
        username_repo = "/".join(url_parts[-2:])

    if username_repo.endswith(".git"):
        return username_repo[:-4]

    return username_repo


def filter_empty_string(array):
    return [a for a in array if len(a) > 0]


def origin_url():
    return _run_git_command("config --get remote.origin.url")


def git_directory():
    return _run_git_command("rev-parse -q --git-dir")


def pr_message_file():
    return os.path.join(git_directory(), "PULLREQUEST_EDITMSG")


def last_commit_message():
    message = _run_git_command("log --format=%B -n 1")
    return commit_from_string(message)


def _get_last_branch():
    return _run_git_command("rev-parse --abbrev-ref @{-1}")


def _get_main_branch():
    try:
        subprocess.check_call(
            ["git", "show", "origin/main"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return "main"
    except subprocess.CalledProcessError:
        return "master"


def _get_comment_char():
    try:
        return (
            subprocess.check_output(
                ["git", "config", "core.commentChar"],
                stderr=subprocess.DEVNULL,
            )
            .strip()
            .decode("utf-8")
        )
    except subprocess.CalledProcessError:
        return "#"


def commit_from_string(string):
    values = [x.strip() for x in string.split("\n", 1)]
    if len(values) < 2:
        values.append("")
    return values


def pr_message(no_edit):
    title, body = last_commit_message()
    if no_edit:
        return title, body

    file_path = pr_message_file()

    comment_char = _get_comment_char()
    with open(file_path, "w") as f:
        f.write(
            f"""{title}

{body}

{comment_char} The first line will be the title of the PR
{comment_char} Anything below the first line will be the body
"""
        )

    editor = os.getenv("EDITOR") or "vim"
    if "vi" in editor:
        command = f"{editor} -c 'set ft=gitcommit' '{file_path}'"
    else:
        command = f"{editor} '{file_path}'"

    code = os.system(command)
    if code != 0:
        sys.exit("Not submitting PR")

    with open(file_path) as f:
        text = f.read()

    lines = text.split("\n")
    lines = [x for x in lines if not x.startswith(comment_char)]
    text = "\n".join(lines)
    if not text.strip():
        sys.exit("Not submitting with empty message")

    return commit_from_string(text)


def open_existing_pr(username, password, api_url, local, remote):
    print("Opening existing PR")
    payload = {"head": local, "base": remote}
    r = requests.get(
        api_url,
        auth=(username, password),
        headers=HEADERS,
        data=json.dumps(payload),
    )
    if r.status_code == 200:
        pr = r.json()[0]
        webbrowser.open_new_tab(pr["html_url"])


def _has_unrecoverable_error(error_json):
    errors = error_json["errors"]
    if any(error.get("code") == "invalid" for error in errors):
        return True

    return False


def _enable_automerge(
    pr_id: str,
    squash: bool,
    title: str,
    body: str,
    username: str,
    password: str,
) -> None:
    input_str = f"""{{
        pullRequestId: "{pr_id}",
        mergeMethod: REBASE
    }}"""
    if squash:
        input_str = f"""{{
          commitBody: "{body}",
          commitHeadline: "{title}",
          pullRequestId: "{pr_id}",
          mergeMethod: SQUASH
      }}"""
    r = requests.post(
        "https://api.github.com/graphql",
        auth=(username, password),
        data=json.dumps(
            {
                "query": f"""mutation EnableAutoMerge {{
    enablePullRequestAutoMerge(input: {input_str}) {{
      actor {{
        login
      }}
    }}
  }}"""
            }
        ),
    )

    errors = r.json().get("errors")
    if r.status_code > 399 or errors:
        print(f"warning: filed to enable automerge: {errors}", file=sys.stderr)


def main(args):
    remote = args.branch
    if remote == "-":
        remote = _get_last_branch()
    elif not remote:
        remote = _get_main_branch()

    title, body = pr_message(args.no_edit)
    username, password = credentials.credentials()
    local = current_branch_name()
    if local.split(":")[-1] == remote:
        sys.exit("Cannot submit PR from the same branch")
    api_url = URL % repo_with_username()
    payload = {"title": title, "body": body, "base": remote, "head": local}
    if args.draft and not (args.merge_rebase or args.merge_squash):
        payload["draft"] = True

    r = requests.post(
        api_url,
        auth=(username, password),
        headers=HEADERS,
        data=json.dumps(payload),
    )
    response_json = r.json()
    if r.status_code == 201:
        if not args.no_open:
            webbrowser.open_new_tab(response_json["html_url"])

        if args.merge_squash or args.merge_squash:
            _enable_automerge(
                response_json["node_id"],
                args.merge_squash,
                title,
                body,
                username,
                password,
            )
    elif r.status_code == 422:
        if _has_unrecoverable_error(r.json()):
            print(f"error: failed to create PR: {r.json()}")
        else:
            open_existing_pr(username, password, api_url, local, remote)
    else:
        try:
            error_message = response_json["errors"][0]["message"]
            print(error_message)
        except KeyError:
            print(response_json)
            raise

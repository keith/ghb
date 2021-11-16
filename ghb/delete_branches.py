#
# Delete branches matching given prefixes that don't have open PRs. This is
# useful to cleanup, especially automated, stale branches
#
# Usage: ghb delete-branches prefix1 prefix2
#
import subprocess
from typing import List
from typing import Set

import requests

from .helpers import credentials


def _get_open_pr_branches(repo: str) -> Set[str]:
    url = f"https://api.github.com/repos/{repo}/pulls"
    user, password = credentials.credentials()
    branches = set()
    while url:
        response = requests.get(url, auth=(user, password))
        if response.status_code != 200:
            raise SystemExit(f"error: failed to fetch PRs: {response.text}")

        for pr in response.json():
            branches.add(pr["head"]["ref"])

        url = response.links.get("next", {}).get("url", None)

    return branches


def _get_filter_args(prefixes: List[str]) -> List[str]:
    return [f"origin/{prefix}*" for prefix in prefixes]


def _format_local_branch(branch: str) -> str:
    branch = branch.strip()
    if branch.startswith("origin/"):
        branch = branch[len("origin/") :]
    else:
        raise SystemExit(f"error: unexpected local branch format: {branch}")
    return branch


def _get_local_branches(prefixes: List[str]) -> Set[str]:
    # git branch --remotes --list prefixes
    output = subprocess.check_output(
        ["git", "branch", "--remotes", "--list"] + _get_filter_args(prefixes)
    ).decode("utf-8")
    return {_format_local_branch(branch) for branch in output.splitlines()}


def _delete_branches(branches: List[str]) -> None:
    batch_size = 100
    for i in range(0, len(branches), batch_size):
        batch = branches[i : i + batch_size]
        subprocess.check_call(["git", "push", "origin", "--delete"] + batch)


def main(args) -> None:
    prefixes = args.branch_prefixes
    deletable_branches = _get_local_branches(prefixes) - _get_open_pr_branches(
        args.repo
    )

    if not deletable_branches:
        print("No branches to delete!")
        return

    _delete_branches(list(deletable_branches))

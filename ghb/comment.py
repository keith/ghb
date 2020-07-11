#
# Comments on issues
# Usage: ghb comment BODY ISSUES...
#   You can also pass a file list as an issue where the argument starts with
#   a '@' and each line eof the file is a URL
#

from typing import List
import argparse
import json
import re

import requests

from .helpers import credentials

_ISSUE_RE = re.compile(
    r"https?://[^/]+/(?P<owner>[^/]+)/(?P<repo>[^/]+)/(issues|pull)/(?P<number>\d+)"
)


NETRC_MACHINE = "api.github.com"


def _comment(owner: str, repo: str, number: str, body: str) -> None:
    user, password = credentials.credentials(NETRC_MACHINE)
    url = (
        f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments"
    )
    response = requests.post(
        url, auth=(user, password), data=json.dumps({"body": body})
    )
    if response.status_code != 201:
        raise SystemExit(
            "error: failed to comment on {}: {}".format(
                url, json.dumps(response.json())
            )
        )

    print(f"Commented: {url}")


def _issue_urls(issues_arg: List[str]) -> List[str]:
    urls = []
    for issue in issues_arg:
        if issue.startswith("@"):
            urls.extend(open(issue[1:]).read().splitlines())
        else:
            urls.append(issue)
    return urls


def main(options: argparse.Namespace) -> None:
    issue_urls = _issue_urls(options.issues)
    for issue in issue_urls:
        if match := _ISSUE_RE.match(issue):
            _comment(
                match.group("owner"),
                match.group("repo"),
                match.group("number"),
                options.body,
            )
        else:
            raise SystemExit(
                "error: could not parse issue URL: {}".format(issue)
            )

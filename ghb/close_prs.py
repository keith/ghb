#
# Bulk close pull requests matching some criteria. This is especially useful
# for cleaning up old automated pull requests and can also be used with ghb
# delete-branches
#
# Usage: ghb close-prs author base
#

from typing import Set
import argparse
import json
import sys

import requests

from .helpers import credentials


NETRC_MACHINE = "api.github.com"


def _get_open_prs(repo: str, author: str, base: str) -> Set[str]:
    params = {"state": "open", "per_page": "100", "base": base}
    url = f"https://api.github.com/repos/{repo}/pulls"
    user, password = credentials.credentials(NETRC_MACHINE)
    urls = set()
    while url:
        response = requests.get(url, auth=(user, password), params=params)
        if response.status_code != 200:
            raise SystemExit(f"error: failed to fetch PRs: {response.text}")

        for pr in response.json():
            assert pr["base"]["ref"] == base
            assert pr["state"] == "open"
            if pr["user"]["login"].lower() == author.lower():
                urls.add(pr["url"])

        url = response.links.get("next", {}).get("url", None)

    return urls


def main(args: argparse.Namespace) -> None:
    user, password = credentials.credentials(NETRC_MACHINE)
    open_prs = _get_open_prs(args.repo, args.author, args.base)
    data = json.dumps({"state": "closed"})
    failed = False
    for pr_url in open_prs:
        response = requests.patch(pr_url, auth=(user, password), data=data)
        if response.status_code != 200:
            print(f"warning: failed to close {pr_url}")
            failed = True

    if failed:
        sys.exit(1)

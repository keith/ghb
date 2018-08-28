#!/usr/bin/env python3
#
# Clear comments on a pull request
# Usage: ghb clear-comments USER/REPO PR_NUMBER
#

from helpers import credentials
from requests import get, delete
import argparse
import signal
import sys

PULLS_URL = "https://api.github.com/repos/%s/pulls/%s/comments"
PULLS_DELETE_URL = "https://api.github.com/repos/%s/pulls/comments/%s"
ISSUES_URL = "https://api.github.com/repos/%s/issues/%s/comments"
ISSUES_DELETE_URL = "https://api.github.com/repos/%s/issues/comments/%s"
NETRC_MACHINE = "api.github.com"


def signal_handle(sig, frame):
    sys.exit(0)


def main(options):
    repo = options["repo"]
    pr_number = options["pr"]
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = get(PULLS_URL % (repo, pr_number), auth=(user, password),
            headers=headers)
    if r.status_code != 200:
        print("Failed to retrieve PR comments: %d" % r.status_code)
        sys.exit(1)

    pr_comments = r.json()

    r = get(ISSUES_URL % (repo, pr_number), auth=(user, password),
            headers=headers)
    if r.status_code != 200:
        print("Failed to retrieve issue comments: %d" % r.status_code)
        sys.exit(1)

    issue_comments = r.json()

    for pr_comment in pr_comments:
        r = delete(PULLS_DELETE_URL % (repo, pr_comment["id"]),
                   auth=(user, password), headers=headers)
        if r.status_code != 204:
            print("Failed to delete PR comment: %d" % r.status_code)

    for issue_comment in issue_comments:
        r = delete(ISSUES_DELETE_URL % (repo, issue_comment["id"]),
                   auth=(user, password), headers=headers)
        if r.status_code != 204:
            print("Failed to delete issue comment: %d" % r.status_code)


signal.signal(signal.SIGINT, signal_handle)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Protect/Unprotect a branch")
    parser.add_argument("repo", help="the user/repo to edit")
    parser.add_argument("pr", help="the PR number to clear")
    ns = parser.parse_args()
    main(vars(ns))

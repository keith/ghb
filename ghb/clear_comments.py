#
# Clear comments on a pull request
# Usage: ghb clear-comments USER/REPO PR_NUMBER
#

import sys

import requests

from .helpers import credentials

PULLS_URL = "https://api.github.com/repos/%s/pulls/%s/comments"
PULLS_DELETE_URL = "https://api.github.com/repos/%s/pulls/comments/%s"
ISSUES_URL = "https://api.github.com/repos/%s/issues/%s/comments"
ISSUES_DELETE_URL = "https://api.github.com/repos/%s/issues/comments/%s"
NETRC_MACHINE = "api.github.com"


def main(options):
    repo = options.repo
    pr_number = options.pr
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(PULLS_URL % (repo, pr_number), auth=(user, password),
                     headers=headers)
    if r.status_code != 200:
        print("Failed to retrieve PR comments: %d" % r.status_code)
        sys.exit(1)

    pr_comments = r.json()

    r = requests.get(ISSUES_URL % (repo, pr_number), auth=(user, password),
                     headers=headers)
    if r.status_code != 200:
        print("Failed to retrieve issue comments: %d" % r.status_code)
        sys.exit(1)

    issue_comments = r.json()

    for pr_comment in pr_comments:
        r = requests.delete(PULLS_DELETE_URL % (repo, pr_comment["id"]),
                            auth=(user, password), headers=headers)
        if r.status_code != 204:
            print("Failed to delete PR comment: %d" % r.status_code)

    for issue_comment in issue_comments:
        r = requests.delete(ISSUES_DELETE_URL % (repo, issue_comment["id"]),
                            auth=(user, password), headers=headers)
        if r.status_code != 204:
            print("Failed to delete issue comment: %d" % r.status_code)

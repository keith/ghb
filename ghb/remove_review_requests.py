#
# Remove requested reviewers from a PR
# Usage: ghb remove-reqview-requests USER/REPO PR_NUMBER
#
#

import json

import requests

from .helpers import credentials


URL = "https://api.github.com/repos/%s/pulls/%s/requested_reviewers"


def main(options):
    username, password = credentials.credentials()
    headers = {"Accept": "application/vnd.github+json"}

    r = requests.get(
        URL % (options.repo, options.pr),
        auth=(username, password),
        headers=headers,
    )
    print(json.dumps(r.json()))
    r.raise_for_status()
    usernames = [x["login"] for x in r.json()["users"]]
    r2 = requests.delete(
        URL % (options.repo, options.pr),
        auth=(username, password),
        headers=headers,
        json={"reviewers": usernames},
    )
    print(json.dumps(r2.json()))
    r2.raise_for_status()

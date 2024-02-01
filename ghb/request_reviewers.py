#
# Request reviews on a PR
# Usage: ghb request-reviewers USER/REPO PR_NUM USERS...
#
#

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
    r = requests.post(
        URL % (options.repo, options.pr),
        auth=(username, password),
        headers=headers,
        json={"reviewers": options.users},
    )
    if r.status_code == 201:
        print("Success", r.status_code)
        print(
            "Requested reviewers: ",
            [x["login"] for x in r.json()["requested_reviewers"]],
        )
    else:
        # Currently not sure about what errors can be produced
        print(f"Error. HTTP Code: {r.status_code} JSON: {r.json()}")

#!/usr/bin/env python3
#
# Adds an approval PR review to a pull request
# Usage: ghb approve PR_URL
#

from helpers import credentials
from helpers import pr
import argparse
import json
import requests
import sys

NETRC_MACHINE = "api.github.com"
URL = "https://api.github.com/repos/%s/pulls/%s/reviews"


def main(pull_request):
    repo, number = pr.extract_info(pull_request)
    user, password = credentials.credentials(NETRC_MACHINE)
    params = {"event": "APPROVE"}
    headers = {"Accept": "application/vnd.github.black-cat-preview+json"}
    response = requests.post(URL % (repo, number), auth=(user, password),
                             data=json.dumps(params), headers=headers)
    if response.status_code != 200:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approve a PR")
    parser.add_argument("pr", help="the PR to approve")
    arguments = parser.parse_args()

    try:
        main(arguments.pr)
    except KeyboardInterrupt:
        sys.exit(1)

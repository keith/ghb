#
# Adds an approval PR review to a pull request
# Usage: ghb approve PR_URL
#

import json
import sys

import requests

from .helpers import credentials
from .helpers import pr

NETRC_MACHINE = "api.github.com"
URL = "https://api.github.com/repos/%s/pulls/%s/reviews"


def main(args):
    pull_request = args.pr
    repo, number = pr.extract_info(pull_request)
    user, password = credentials.credentials(NETRC_MACHINE)
    params = {"event": "APPROVE"}
    headers = {"Accept": "application/vnd.github.black-cat-preview+json"}
    response = requests.post(
        URL % (repo, number),
        auth=(user, password),
        data=json.dumps(params),
        headers=headers,
    )
    if response.status_code != 200:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        sys.exit(1)

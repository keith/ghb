#
# Assigns the currently authorized user to a pull request
# Usage: ghb assignme PR_URL
#
import json
import sys

import requests

from .helpers import credentials
from .helpers import pr

NETRC_MACHINE = "api.github.com"
URL = "https://api.github.com/repos/%s/issues/%s/assignees"


def main(args):
    repo, number = pr.extract_info(args.pr)
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {"assignees": [user]}
    response = requests.post(
        URL % (repo, number),
        auth=(user, password),
        data=json.dumps(params),
        headers=headers,
    )
    if response.status_code != 201:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        sys.exit(1)

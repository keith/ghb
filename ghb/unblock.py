#
# Unblock a github user
# Note: your token needs 'user' access for this API
# Usage: ghb unblock USER
#
import sys

import requests

from .helpers import credentials

BLOCK_URL = "https://api.github.com/user/blocks/%s"
NETRC_MACHINE = "api.github.com"


def main(args):
    block_user = args.user
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {
        "Accept": "application/vnd.github.giant-sentry-fist-preview+json"
    }
    r = requests.delete(
        BLOCK_URL % block_user, auth=(user, password), headers=headers
    )
    if r.status_code == 404:
        print("User '%s' doesn't exist" % block_user)
        sys.exit(1)
    elif r.status_code != 204:
        print("Failed to block user: %d" % r.status_code)
        sys.exit(1)

#
# Get the list of users you've blocked on github
# Note: your token needs 'user' access for this API
# Usage: ghb get-blocks
#

import sys

import requests

from helpers import credentials

URL = "https://api.github.com/user/blocks"
NETRC_MACHINE = "api.github.com"


def main(_):
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {
        'Accept': 'application/vnd.github.giant-sentry-fist-preview+json'
    }
    r = requests.get(URL, auth=(user, password), headers=headers)
    if r.status_code != 200:
        print("Failed to get blocked users: %d" % r.status_code)
        print(r.json())
        sys.exit(1)

    for blob in r.json():
        print(blob["login"])

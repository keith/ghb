#!/usr/bin/env python3
#
# Block a github user
# Note: your token needs 'user' access for this API
# Usage: ghb block USER
#

from helpers import credentials
from requests import put
import argparse
import signal
import sys

BLOCK_URL = "https://api.github.com/user/blocks/%s"
NETRC_MACHINE = "api.github.com"


def signal_handle(sig, frame):
    sys.exit(0)


def main(block_user):
    user, password = credentials.credentials(NETRC_MACHINE)
    headers = {
        'Accept': 'application/vnd.github.giant-sentry-fist-preview+json'
    }
    r = put(BLOCK_URL % block_user, auth=(user, password), headers=headers)
    if r.status_code == 422:
        print("User '%s' is already blocked" % block_user)
        sys.exit(1)
    elif r.status_code == 404:
        print("User '%s' doesn't exist" % block_user)
        sys.exit(1)
    elif r.status_code != 204:
        print("Failed to block user: %d" % r.status_code)
        sys.exit(1)

signal.signal(signal.SIGINT, signal_handle)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Block a github user")
    parser.add_argument("user", help="the user to block")
    main(parser.parse_args().user)

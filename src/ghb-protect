#!/usr/bin/env python3
#
# Enable/disable GitHub protected branch status
# Usage: ghb protect USER/REPO BRANCH [--disable] [STATUSES...]
#
# Example: ghb protect keith ghb master travis
# This would enable protection on master forcing the travis build to pass
#
# Note: Requiring administrators to go through protection is currently hardcoded
#

import signal
import sys
from argparse import ArgumentParser
from helpers import credentials
from json import dumps
from requests import patch


URL = "https://api.github.com/repos/%s/branches/%s"
NETRC_MACHINE = "api.github.com"


def signal_handle(sig, frame):
    sys.exit(1)


def url_from_options(options):
    return URL % (options["repo"], options["branch"])


def data_for_options(options):
    enabled = not options["disable"]
    data = {"protection": {"enabled": enabled}}
    statuses = options["statuses"]
    if statuses:
        data["protection"]["required_status_checks"] = {
            "enforcement_level": "everyone",
            "contexts": statuses,
        }

    return data


def main(options):
    username, password = credentials.credentials(NETRC_MACHINE)
    headers = {'Accept': 'application/vnd.github.loki-preview'}
    payload = dumps(data_for_options(options))
    r = patch(url_from_options(options),
              auth=(username, password),
              headers=headers,
              data=payload)
    if r.status_code == 200:
        print("Success")
    else:
        # Currently not sure about what errors can be produced
        print("Error. HTTP Code: %s JSON: %s" % (r.status_code, r.json()))

signal.signal(signal.SIGINT, signal_handle)
if __name__ == '__main__':
    parser = ArgumentParser(description="Protect/Unprotect a branch")
    parser.add_argument("--disable", help="disable protection",
                        action="store_true", default=False)
    parser.add_argument("repo", help="the user/repo to edit")
    parser.add_argument("branch", help="The name of the branch")
    parser.add_argument("statuses", nargs="*",
                        help="The required status checks")
    ns = parser.parse_args()
    main(vars(ns))

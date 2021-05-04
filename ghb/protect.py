#
# Enable/disable GitHub protected branch status
# Usage: ghb protect USER/REPO BRANCH [--disable] [STATUSES...]
#
# Example: ghb protect keith ghb master travis
# This would enable protection on master forcing the travis build to pass
#
# Note: Requiring administrators to go through protection is currently hardcoded
#
import json

import requests

from .helpers import credentials


URL = "https://api.github.com/repos/%s/branches/%s"


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


def main(args):
    options = vars(args)
    username, password = credentials.credentials()
    headers = {"Accept": "application/vnd.github.loki-preview"}
    payload = json.dumps(data_for_options(options))
    r = requests.patch(
        url_from_options(options),
        auth=(username, password),
        headers=headers,
        data=payload,
    )
    if r.status_code == 200:
        print("Success")
    else:
        # Currently not sure about what errors can be produced
        print(f"Error. HTTP Code: {r.status_code} JSON: {r.json()}")

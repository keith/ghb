#
# Unblock a github user
# Note: your token needs 'user' access for this API
# Usage: ghb unblock USER
#
import json
import sys

import requests

from .helpers import credentials

_STATUS_URL = "https://api.github.com/repos/{}/statuses/{}"
_GET_STATUS_URL = (
    "https://api.github.com/repos/{}/commits/{}/status?per_page=100"
)


def main(args):
    user, password = credentials.credentials()
    response = requests.get(
        _GET_STATUS_URL.format(args.repo, args.sha), auth=(user, password)
    )
    if response.status_code != 200:
        sys.exit(
            "error: failed response: {} {}".format(
                response.status_code, response.json()
            )
        )

    blob = response.json()
    if blob["state"] == "success":
        sys.exit("All statuses are successful")

    for status in response.json()["statuses"]:
        if status["state"] == "success":
            continue

        print(status["context"])
        body = {
            "context": status["context"],
            "description": "{} - faked".format(status["description"]),
            "state": "success",
            "target_url": status["target_url"],
        }

        response = requests.post(
            status["url"], data=json.dumps(body), auth=(user, password)
        )
        if response.status_code != 201:
            sys.exit(
                "error: failed to set status {} {}".format(
                    response.status_code, response.json()
                )
            )

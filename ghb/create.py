#
# Create new GitHub repos
# Usage: ghb create NAME [-d/--description repo description]
#                        [-u/--url the homepage URL]
#                        [-p/--private make the repo private (default public)]
#                        [-w/--wiki enable wiki (off by default)]
#                        [--no-issues disable issues]
#                        [--no-downloads disable downloads]
#

import json
import webbrowser

import requests

from .helpers import credentials

URL = "https://api.github.com/user/repos"
NETRC_MACHINE = "api.github.com"


def main(args):
    username, password = credentials.credentials(NETRC_MACHINE)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    payload = json.dumps(vars(args))
    r = requests.post(URL, auth=(username, password), headers=headers,
                      data=payload)
    response_json = r.json()
    if r.status_code == 201:
        print("Success")
        webbrowser.open_new_tab(response_json["html_url"])
    else:
        print("Error")
        print(json.dumps(response_json, indent=2))

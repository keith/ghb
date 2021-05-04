#
# Watch a GitHub repo
# Usage: ghb watch user/repo
#
import json
import re
import sys

import requests

from .helpers import credentials

WATCH = "https://api.github.com/repos/%s/subscription"


def main(args):
    repo = args.repo
    regex = re.compile(r"\w+/\w+")
    if not regex.match(repo):
        print("'%s' is not in the format 'user/repo'" % repo)
        sys.exit(1)

    user, password = credentials.credentials()
    url = WATCH % repo
    body = json.dumps({"subscribed": True})
    r = requests.put(url, data=body, auth=(user, password))
    code = r.status_code
    if code == 200:
        print("Success")
    else:
        print("Failed with code: %d" % code)

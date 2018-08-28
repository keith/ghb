#!/usr/bin/env python3
#
# Get the language breakdown for a repo
# Usage: ghb langs USER/REPO
#

from helpers import credentials
from operator import itemgetter
from requests import get
import argparse
import signal
import sys

URL = "https://api.github.com/repos/%s/languages"
NETRC_MACHINE = "api.github.com"


def signal_handle(sig, frame):
    sys.exit(0)


def total_lines(json):
    return sum(json.values())


def average(total, number):
    avg = round((number / float(total)) * 100, 2)
    return avg


def main(repo):
    get_url = URL % repo
    username, password = credentials.credentials(NETRC_MACHINE)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = get(get_url, auth=(username, password), headers=headers)
    json = r.json()
    if r.status_code != 200:
        sys.exit("Failed with error: %s" % (json["message"]))
    total = total_lines(json)
    averages = {k: average(total, v) for k, v in json.items()}
    averages = sorted(averages.items(), key=itemgetter(1), reverse=True)
    for t in averages:
        print("%15s: %8.2f%%" % (t[0], t[1]))


signal.signal(signal.SIGINT, signal_handle)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Get the language breakdown for a repo")
    parser.add_argument("repo", help="the user/repo")
    ns = parser.parse_args()
    main(vars(ns)["repo"])

#!/usr/bin/env python3
#
# Open your unread GitHub notifications in new tabs
# Usage: ghb notifications
#

import signal
import sys
from helpers import credentials
from requests import get
from webbrowser import open_new_tab

URL = "https://api.github.com/notifications"
NETRC_MACHINE = "api.github.com"


def signal_handle(sig, frame):
    sys.exit(0)


def open_pull_requests():
    user, password = credentials.credentials(NETRC_MACHINE)
    r = get(URL, auth=(user, password))
    json = r.json()
    opened = False

    for blob in json:
        notification_url = blob["subject"]["url"]
        r = get(notification_url, auth=(user, password))
        html_url = r.json()["html_url"]
        open_new_tab(html_url)
        opened = True

    if not opened:
        sys.exit("No Unread Notifications")


signal.signal(signal.SIGINT, signal_handle)
if __name__ == "__main__":
    open_pull_requests()

#
# Open your unread GitHub notifications in new tabs
# Usage: ghb notifications
#
import sys
import webbrowser

import requests

from .helpers import credentials

URL = "https://api.github.com/notifications"


def main(_):
    user, password = credentials.credentials()
    r = requests.get(URL, auth=(user, password))
    r.raise_for_status()
    opened = False

    for blob in r.json():
        notification_url = blob["subject"]["url"]
        r = requests.get(notification_url, auth=(user, password))
        html_url = r.json()["html_url"]
        webbrowser.open_new_tab(html_url)
        opened = True

    if not opened:
        sys.exit("No Unread Notifications")

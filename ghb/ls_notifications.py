#
# List your unread GitHub notifications
# Usage: ghb ls-notifications
#
import requests

from .helpers import credentials

URL = "https://api.github.com/notifications"


def main(_):
    user, password = credentials.credentials()
    r = requests.get(URL, auth=(user, password))
    notifications = {}

    for blob in r.json():
        repo_name = blob["repository"]["full_name"]
        api_url = blob["subject"]["url"]
        if not api_url:
            continue
        html_url = (
            api_url.replace("api.", "", 1)
            .replace("/repos", "", 1)
            .replace("/pulls/", "/pull/")
        )
        notification = "\t{} ({})".format(blob["subject"]["title"], html_url)
        notifications.setdefault(repo_name, []).append(notification)

    for name, urls in notifications.items():
        print(name)
        for url in urls:
            print(url)
        print()

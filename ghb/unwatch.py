#
# Unwatch GitHub repos (specifically userful if you accidentally opt in to
# watching hundreds of repos)
#
# Usage: ghb unwatch [-u/--users valid users, never unwatch repos from]
#                    [-i/--ignored ignored repo names, automatically unwatched]
#
# Note: Arguments are comma separated
#
import webbrowser

import requests

from .helpers import credentials

WATCHING = "https://api.github.com/user/subscriptions?page=%s&per_page=100"
UNWATCH = "https://api.github.com/repos/%s/subscription"
HTML_URL = "https://github.com/%s"


def ask(repo):
    i = input("Unwatch " + repo + " y/n/o: ").lower()[0]
    if i.startswith("o"):
        webbrowser.open_new_tab(HTML_URL % repo)
        return ask(repo)

    return i.startswith("y")


def repo_name(repo):
    name = repo["full_name"]
    return [x.lower() for x in name.split("/")]


def is_valid_user(repo, valid_users):
    user, _ = repo_name(repo)
    return user not in valid_users


def main(args):
    valid_users = [x.lower() for x in args.users.split(",")]
    ignored_repos = [x.lower() for x in args.ignored.split(",")]
    user, password = credentials.credentials()
    json = []
    count = 1
    while True:
        url = WATCHING % count
        r = requests.get(url, auth=(user, password))
        j = r.json()
        if j:
            json += j
            count += 1
        else:
            break

    json = [x for x in json if is_valid_user(x, valid_users)]
    print("Asking about %s repos" % len(json))

    for repo in json:
        user, name = repo_name(repo)
        full_name = repo["full_name"]
        delete = None
        if name in ignored_repos:
            delete = True

        if delete is None:
            try:
                delete = ask(full_name)
            except KeyboardInterrupt:
                break

        if delete:
            url = UNWATCH % full_name
            requests.delete(url, auth=(user, password))

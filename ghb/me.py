#
# Open your GitHub profile
# Usage: ghb me
#
import webbrowser

from .helpers import credentials

URL = "https://github.com/%s"


def main(_):
    username, _ = credentials.credentials()
    webbrowser.open_new_tab(URL % username)

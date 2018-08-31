#
# Open your GitHub profile
# Usage: ghb me
#

import webbrowser

from helpers import credentials

URL = "https://github.com/%s"
NETRC_MACHINE = "api.github.com"


def main(_):
    username, _ = credentials.credentials(NETRC_MACHINE)
    webbrowser.open_new_tab(URL % username)

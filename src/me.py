#!/usr/bin/env python3
#
# Open your GitHub profile
# Usage: ghb me
#

from helpers import credentials
from webbrowser import open_new_tab

URL = "https://github.com/%s"
NETRC_MACHINE = "api.github.com"


def main():
    username, _ = credentials.credentials(NETRC_MACHINE)
    open_new_tab(URL % username)

if __name__ == '__main__':
    main()

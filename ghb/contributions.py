#
# Print your contributions for the current day
# Usage: ghb contributions
#

import html.parser

import requests

from .helpers import credentials

URL = "https://github.com/users/%s/contributions"
NETRC_MACHINE = "github.com"


class CustomHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.rects = []

    def handle_starttag(self, tag, attrs):
        if tag == "rect":
            self.rects.append(attrs)


def pluralize(number):
    if number == 1:
        return ""
    return "s"


def main(_):
    username, _ = credentials.credentials(NETRC_MACHINE)
    r = requests.get(URL % username)
    parser = CustomHTMLParser()
    parser.feed(r.text)
    d = dict(parser.rects[-1])
    number = d["data-count"]
    date = d["data-date"]
    print("You have %s contribution%s on %s" %
          (number, pluralize(number), date))

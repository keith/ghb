#
# Download the first asset from the newest release from a GitHub repo
# Usage: ghb download-release USER/REPO [-f/--filename only print the filename]
#

import sys

import requests

URL = "https://api.github.com/repos/%s/releases"


def extension(t, default):
    if t == "zip":
        return t
    if t == "x-gzip":
        return "tar.gz"

    return default


def print_filename(filename, only_filename):
    if only_filename:
        print(filename)
    else:
        print("Release saved to %s" % filename)


def main(args):
    repo = args.repo
    r = requests.get(URL % repo)
    response_json = r.json()
    if not response_json:
        print("No releases for %s" % repo)
        sys.exit(1)

    newest = response_json[0]
    assets = newest["assets"]
    first_asset = assets[0]
    asset_url = first_asset["browser_download_url"]
    content_type = first_asset["content_type"].split("/")[-1]
    default = first_asset["name"].split(".")[-1]
    headers = {"Accept": "application/octet-stream"}
    r = requests.get(asset_url, headers=headers, stream=True)
    filename = "release.%s" % extension(content_type, default)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
            f.flush()

    print(filename)

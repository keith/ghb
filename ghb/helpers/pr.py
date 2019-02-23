import re
import sys

REGEX = re.compile(
    r"(https?://github.com/)?(.*/.*)/pull/(\d+)/?(commits|files)?"
)


def extract_info(pr):
    match = REGEX.match(pr)
    if not match:
        print("Failed to match '{}'".format(pr))
        sys.exit(1)

    repo, number = match.group(2), match.group(3)
    if not repo or not number:
        print("Failed to extract repo info from '{}'".format(pr))
        sys.exit(1)

    return repo, number

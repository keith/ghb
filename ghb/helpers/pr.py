import re
import sys

REGEX = re.compile(
    r"(https?://github.com/)?(.*/.*)/pull/(\d+)/?(commits|files)?"
)


def extract_info(pr):
    match = REGEX.match(pr)
    if not match:
        print(f"Failed to match '{pr}'")
        sys.exit(1)

    repo, number = match.group(2), match.group(3)
    if not repo or not number:
        print(f"Failed to extract repo info from '{pr}'")
        sys.exit(1)

    return repo, number

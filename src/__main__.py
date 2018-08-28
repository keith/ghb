import argparse
import signal
import sys

from . import approve
from . import assignme
from . import block
from . import clear_comments
from . import contributions
from . import create
from . import unwatch
from . import watch


def _signal_handle(sig, frame):
    sys.exit(0)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="subcommand")
subparsers.required = True

approve_parser = subparsers.add_parser("approve", help="Approve a PR")
approve_parser.add_argument("pr", help="the PR to approve")

assignme_parser = subparsers.add_parser(
    "assignme", help="Assign yourself to a PR")
assignme_parser.add_argument("pr", help="The PR to assign yourself to")

block_parser = subparsers.add_parser("block", help="foobar")
block_parser.add_argument("user", help="the user to block")

clear_comments_parser = subparsers.add_parser(
    "clear-comments", help="Protect/Unprotect a branch")
clear_comments_parser.add_argument("repo", help="the user/repo to edit")
clear_comments_parser.add_argument("pr", help="the PR number to clear")

contributions_parser = subparsers.add_parser(
    "contributions", help="Get your contribution count for today")

create_parser = subparsers.add_parser("create",
                                      help="Create a new GitHub repo")
create_parser.add_argument("name", help="the name of the repo")
create_parser.add_argument(
    "-d", "--description", help="the description of the repo")
create_parser.add_argument(
    "-u", "--url", help="the homepage for the repo", dest="homepage")
create_parser.add_argument(
    "-p", "--private", action="store_true", help="make the repo private",
    default=False)
create_parser.add_argument(
    "-w", "--wiki", action="store_true", help="enable wikis", default=False,
    dest="has_wiki")
create_parser.add_argument(
    "--no-issues", action="store_false", help="disable issues", default=True,
    dest="has_issues")
create_parser.add_argument(
    "--no-downloads", action="store_false", help="disable downloads",
    default=True, dest="has_downloads")

watch_parser = subparsers.add_parser("watch", help="Watch GitHub repos")
watch_parser.add_argument("repo", help="the user/repo to watch")

unwatch_parser = subparsers.add_parser("unwatch", help="Unwatch GitHub repos")
unwatch_parser.add_argument("-u", "--users", help="comma separated valid users. Repos from these users are never unwatched", default="")
unwatch_parser.add_argument("-i", "--ignored", help="command separated ignored repo names. Repos from this list are automatically unwatched", default="")

args = parser.parse_args()
print(args)

commands = {
    "approve": approve.main,
    "assignme": assignme.main,
    "block": block.main,
    "clear-comments": clear_comments.main,
    "contributions": contributions.main,
    "create": create.main,
    "watch": watch.main,
    "unwatch": unwatch.main,
}

signal.signal(signal.SIGINT, _signal_handle)
commands[args.subcommand](args)

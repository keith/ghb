import argparse
import signal
import sys

from . import approve
from . import block
from . import clear_comments


def _signal_handle(sig, frame):
    sys.exit(0)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="subcommand")
subparsers.required = True

approve_parser = subparsers.add_parser("approve", help="Approve a PR")
approve_parser.add_argument("pr", help="the PR to approve")

block_parser = subparsers.add_parser("block", help="foobar")
block_parser.add_argument("user", help="the user to block")

clear_comments_parser = subparsers.add_parser(
    "clear-comments", help="Protect/Unprotect a branch")
clear_comments_parser.add_argument("repo", help="the user/repo to edit")
clear_comments_parser.add_argument("pr", help="the PR number to clear")

args = parser.parse_args()
print(args)

commands = {
    "approve": approve.main,
    "block": block.main,
    "clear-comments": clear_comments.main,
}

signal.signal(signal.SIGINT, _signal_handle)
commands[args.subcommand](args)

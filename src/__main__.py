#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
block_parser = subparsers.add_parser("block", help="foobar")
block_parser.add_argument("user")

parser.parse_args()

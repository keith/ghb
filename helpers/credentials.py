#!/usr/bin/env python

import netrc
import sys


def credentials(machine):
    n = netrc.netrc()
    auth = n.authenticators(machine)
    if auth is None:
        sys.exit("Add %s to your ~/.netrc" % machine)

    user = auth[0] or auth[1]
    password = auth[2]

    if user is None or password is None:
        sys.exit("Invalid netrc entry for %s" % machine)

    return user, password

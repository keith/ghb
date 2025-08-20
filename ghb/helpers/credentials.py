import netrc

_MACHINE = "api.github.com"
_EXAMPLE_CONTENTS = f"""\
machine {_MACHINE}
  login GITHUB_USERNAME
  password GITHUB_API_TOKEN # Generate from https://github.com/settings/tokens
"""


def credentials() -> tuple[str, str]:
    try:
        n = netrc.netrc()
    except FileNotFoundError:
        raise SystemExit(
            f"error: ~/.netrc not found, create one with these contents:\n\n{_EXAMPLE_CONTENTS}"
        )
    except netrc.NetrcParseError as e:
        if "too permissive" in e.msg:
            raise SystemExit(
                f"error: ~/.netrc is too permissive, run 'chmod 600 ~/.netrc'"
            )
        raise SystemExit(
            f"error: ~/.netrc has invalid contents, you need something like this:\n\n{_EXAMPLE_CONTENTS}"
        )

    auth = n.authenticators(_MACHINE)
    if not auth:
        raise SystemExit(
            f"error: add {_MACHINE} like this:\n\n{_EXAMPLE_CONTENTS}"
        )

    user = auth[0] or auth[1]
    password = auth[2]

    if user is None or password is None:
        raise SystemExit(f"error: invalid netrc entry for {_MACHINE}")

    return user, password

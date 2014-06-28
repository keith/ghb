# gh

Not [the other gh](https://github.com/jingweno/gh).

This is a small set of scripts for working with github. Unlike hub or
the other gh the purpose of this is not to override `git` and add
functionality on top of that. Instead this uses a git like method of
looking for executables named `gh-*` and nesting them under the `gh`
command. This allows you to create simple single purpose scripts in any
language.

Current commands:

- [create](https://github.com/Keithbsmiley/gh/blob/master/gh-create),
create github repos.

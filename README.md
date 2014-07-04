# gh

Not [the other gh](https://github.com/jingweno/gh).

This is a small set of scripts for working with github. Unlike hub or
the other gh the purpose of this is not to override `git` and add
functionality on top of that. Instead this uses a git like method of
looking for executables named `gh-*` and nesting them under the `gh`
command. This allows you to create simple single purpose scripts in any
language.

## Current commands

- [create](https://github.com/Keithbsmiley/gh/blob/master/gh-create),
create github repos.
- [contributions](https://github.com/Keithbsmiley/gh/blob/master/gh-contributions),
view the number of contributions you've made today

### Installation

You can put these anywhere in your $PATH. If you'd like you can use my
[homebrew
formula](https://github.com/Keithbsmiley/homebrew-formulae/blob/master/Formula/gh.rb)
to install gh as well. Note it does not manage all dependencies such as [requests](http://docs.python-requests.org/en/latest/)

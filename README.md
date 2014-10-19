# ghb

This is a small set of scripts for working with github. Unlike hub or
gh the purpose of this is not to override `git` and add functionality
on top of that. Instead this uses a git like method of looking for
executables named `ghb-*` and nesting them under the `ghb` command. This
allows you to create simple single purpose scripts in any language.

## Current commands

- [create](https://github.com/Keithbsmiley/ghb/blob/master/ghb-create),
create github repos.
- [contributions](https://github.com/Keithbsmiley/ghb/blob/master/ghb-contributions),
view the number of contributions you've made today
- [download-release](https://github.com/Keithbsmiley/ghb/blob/master/ghb-download-release),
download the most recent release from a repo
- [notifications](https://github.com/Keithbsmiley/ghb/blob/master/ghb-notifications),
open your unread notifications in the browser


### Installation

You can put these anywhere in your $PATH. If you'd like you can use my
[homebrew
formula](https://github.com/Keithbsmiley/homebrew-formulae/blob/master/Formula/ghb.rb)
to install ghb as well.

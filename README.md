# ghb

This is a small set of scripts for working with github. Unlike hub or gh
the purpose of this is not to override `git` and add functionality on
top of that. Instead this uses a git like method of looking for
executables named `ghb-*` and nesting them under the `ghb` command. This
allows you to create simple single purpose scripts in any language.

## Commands

- [approve](https://github.com/keith/ghb/blob/master/src/ghb-approve),
quickly approve a PR with a GitHub review
- [contributions](https://github.com/keith/ghb/blob/master/src/ghb-contributions),
view the number of contributions you've made today
- [clear-comments](https://github.com/keith/ghb/blob/master/src/ghb-clear-comments),
delete all comments on a pull request
- [create](https://github.com/keith/ghb/blob/master/src/ghb-create),
create github repos.
- [download-release](https://github.com/keith/ghb/blob/master/src/ghb-download-release),
download the most recent release from a repo
- [langs](https://github.com/keith/ghb/blob/master/src/ghb-langs),
get the language breakdown for a repo
- [ls-notifications](https://github.com/keith/ghb/blob/master/src/ghb-ls-notifications),
list your unread notifications
- [me](https://github.com/keith/ghb/blob/master/src/ghb-me),
open your GitHub profile
- [notifications](https://github.com/keith/ghb/blob/master/src/ghb-notifications),
open your unread notifications in the browser
- [pr](https://github.com/keith/ghb/blob/master/src/ghb-pr),
open a PR from the current branch
- [protect](https://github.com/keith/ghb/blob/master/src/ghb-protect),
enable/disable branch protection for a specific repo and branch
- [unwatch](https://github.com/keith/ghb/blob/master/src/ghb-unwatch),
bulk unwatch repos
- [watch](https://github.com/keith/ghb/blob/master/src/ghb-watch),
watch a repo

See the header comment in each individual file for specific usage.

### Installation

```
brew install keith/formulae/ghb
```

Or put everything inside the `src` directory somewhere in your `$PATH`

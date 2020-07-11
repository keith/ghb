# ghb

This is a small set of scripts for working with github. Unlike hub or gh
the purpose of this is not to override `git` and add functionality on
top of that. Instead this uses a git like method of looking for
executables named `ghb-*` and nesting them under the `ghb` command. This
allows you to create simple single purpose scripts in any language.

## Commands

- [approve](ghb/approve.py), quickly approve a PR with a GitHub review
- [assignme](ghb/assignme.py), assign yourself to a PR
- [block](ghb/block.py), block users on GitHub
- [clear-comments](ghb/clear_comments.py), delete all comments on a pull request
- [contributions](ghb/contributions.py), view the number of contributions you've made today
- [create](ghb/create.py), create github repos.
- [download-release](ghb/download_release.py), download the most recent release from a repo
- [get-blocks](ghb/get_blocks.py), get the users you've blocked
- [greenify](ghb/greenify.py), force all statuses on a PR to be gren
- [langs](ghb/langs.py), get the language breakdown for a repo
- [ls-notifications](ghb/ls_notifications.py), list your unread notifications
- [me](ghb/me.py), open your GitHub profile
- [notifications](ghb/notifications.py), open your unread notifications in the browser
- [pr](ghb/pr.py), open a PR from the current branch
- [protect](ghb/protect.py), enable/disable branch protection for a specific repo and branch
- [unblock](ghb/unblock.py), unblock a GitHub user
- [unwatch](ghb/unwatch.py), bulk unwatch repos
- [watch](ghb/watch.py), watch a repo

See the header comment in each individual file for specific usage.

### Installation

```
brew install keith/formulae/ghb
```

Or:

```
pip install .
```

(and `zsh/_ghb` if you want zsh completions)

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
- [close-prs](ghb/close_prs.py), close multiple PRs from a certain author targeting a specific branch
- [comment](ghb/comment.py), comment on a list of issues / PRs
- [contributions](ghb/contributions.py), view the number of contributions you've made today
- [create](ghb/create.py), create github repos.
- [delete-branches](ghb/delete_branches.py), delete stale branches matching some prefix
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
pip install ghb
```

(and install `zsh/_ghb` if you want zsh completions)

### Configuration

To setup authentication for `ghb` you must add a personal access token
to your `~/.netrc` file. You can generate a token
[here](https://github.com/settings/tokens). You should enable the
`repo`, `workflow`, `notifications`, and `user` scopes (you maybe be
able to omit some of those depending on which subcommands you plan to
use).

Then in your `~/.netrc` file add:

```
machine api.github.com
login GITHUB_USERNAME
password TOKEN
```

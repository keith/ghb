# Release process

This is meant to be a quick guide for how new releases are pushed.

1. Make sure `README.md` is updated with any new commands
1. Bump `__version__` in `ghb/__init__.py`
1. Tag the new release
1. Push
1. Update the [brew forumla](https://github.com/keith/homebrew-formulae/blob/master/Formula/ghb.rb)
1. Update the [pypi package](https://pypi.org/project/ghb/1.4.0)
  1. `pip install --upgrade twine setuptools wheel`
  1. `python setup.py sdist bdist_wheel`
  1. `twine upload --repository ghb dist/*`

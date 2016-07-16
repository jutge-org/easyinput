from distutils.core import setup

setup(
  name = 'jutge',
  packages = ['jutge'],
  version = '1.4',
  description = 'Simple functions to read input from Python for problems in Jutge.org.',
  author = 'Jordi Petit',
  author_email = 'jpetit@cs.upc.edu',
  url = 'https://github.com/jutge-org/jutge-python',
  download_url = 'https://github.com/jutge-org/jutge-python/tarball/1.4',
  keywords = ['jutge', 'jutge.org'],
  classifiers = [],
)


# Steps to distribute new version:
#
# Increment version id in "version" and "download_url"
# git commit -a
# git push
# git tag 1.12345 -m "Adds a tag so that we can put this on PyPI.".
# git push --tags origin master
# python setup.py sdist upload
#
# More doc: http://peterdowns.com/posts/first-time-with-pypi.html

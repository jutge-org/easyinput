from distutils.core import setup

import jutge


setup(
    name='jutge',
    packages=['jutge'],
    version=jutge.version,
    description='Simple functions to read input from Python for problems in Jutge.org.',
    author='Jordi Petit',
    author_email='jpetit@cs.upc.edu',
    url='https://github.com/jutge-org/jutge-python',
    download_url='https://github.com/jutge-org/jutge-python/tarball/%s' % jutge.version,
    keywords=['jutge', 'jutge.org', 'education'],
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Education',
    ],
)


# Steps to distribute new version:
#
# Increment version in jutge/__init__py
# git commit -a
# git push
# git tag 1.12345 -m "Release 1.12345"
# git push --tags origin master
# python setup.py sdist upload
#
# More doc: http://peterdowns.com/posts/first-time-with-pypi.html

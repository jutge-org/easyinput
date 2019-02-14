from setuptools import setup

version = "2.1"


setup(
    name='jutge',
    packages=['jutge'],
    install_requires=['future>=0.17', 'enum34'],
    version=version,
    description='Simple functions to read input from Python',
    long_description='Simple functions to read input from Python',
    author='Jordi Petit et al',
    author_email='jpetit@cs.upc.edu',
    url='https://github.com/jutge-org/jutge-python',
    download_url='https://github.com/jutge-org/jutge-python/tarball/{}'.format(version),
    keywords=['jutge', 'jutge.org', 'education', 'input'],
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
        'Programming Language :: Python :: 3.7',
        'Topic :: Education',
    ],

    test_suite='pytest-runner',
    tests_require=['pytest']
)


# Steps to distribute new version:
#
# Increment version in jutge/__init__py
# git commit -a
# git push
# git tag 1.12345 -m "Release 1.12345"
# git push --tags origin master
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
#
# More docs:
# http://peterdowns.com/posts/first-time-with-pypi.html
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56



from setuptools import setup

version = "2.3"


setup(
    name='easyinput',
    packages=['easyinput'],
    install_requires=['future>=0.17', 'enum34'],
    version=version,
    description='Easy functions to read input from Python',
    long_description='Easy functions to read input from Python',
    author='Jordi Petit et al',
    author_email='jpetit@cs.upc.edu',
    url='https://github.com/jutge-org/easy-input',
    download_url='https://github.com/jutge-org/easy-input/tarball/{}'.format(version),
    keywords=['easyinput', 'education', 'input'],
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Education',
    ],

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test'
)


# Steps to distribute new version:
#
# Set new version in easyinput/__init__py and setup.py
# git commit -a
# git push
# git tag 1.12345 -m "Release 1.12345"
# git push --tags origin master
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
#
# More docs:
# http://peterdowns.com/posts/first-time-with-pypi.html
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56



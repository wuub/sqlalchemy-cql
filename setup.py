#!/usr/bin/env python

import os
import sys
from setuptools.command.test import test as TestCommand

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://sqlalchemy-cql.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='sqlalchemy-cql',
    version='0.1.0',
    description='S',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Wojciech Bederski',
    author_email='github@wuub.net',
    url='https://github.com/wuub/sqlalchemy-cql',
    packages=[
        'sqlalchemy_cql',
    ],
    package_dir={'sqlalchemy_cql': 'sqlalchemy_cql'},
    include_package_data=True,
    install_requires=[
        "sqlalchemy",
        "cql"
    ],
    license='MIT',
    zip_safe=False,
    entry_points={
    'sqlalchemy.dialects': [
        "cql = sqlalchemy_cql:CQLDialect"
    ]
    },
    keywords='sqlalchemy_cql',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    tests_require=['pytest>=2.3.5'],
    cmdclass = {'test': PyTest},
)

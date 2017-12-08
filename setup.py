# -*- coding: utf-8 -


from __future__ import with_statement


import io
import os
import sys


from imp import load_source
from setuptools import setup, find_packages
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError


if not hasattr(sys, 'version_info') or sys.version_info < (2, 6, 0, 'final'):
    raise SystemExit("pyobj_Q requires Python 2.6x or later")
ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)
if sys.platform == 'win32' and sys.version_info > (2, 6):
    ext_errors += (IOError,)


simple_http_parser = load_source("pyobj_Q", os.path.join("pyobj_Q", "__init__.py"))
CLASSIFIERS = [
        'Development Status :: 1 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
VERSION = simple_http_parser.__version__
with io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()


def run_setup():
    setup(
        name='pyobj_Q',
        version=VERSION,
        description='support django Q query like for any python object',
        long_description=LONG_DESCRIPTION,
        author='limanman',
        author_email='xmdevops@vip.qq.com',
        license='MIT',
        url='https://github.com/xmdevops/pyobj_Q',
        classifiers=CLASSIFIERS,
        platforms=['any'],
        package_data={'': ['*.md', '*.rst']},
        package_dir={'*': 'pyobj_Q'},
        packages=find_packages()
    )


if __name__ == '__main__':
    run_setup()

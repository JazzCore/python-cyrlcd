# -*- coding: utf-8 -*-

from distutils.core import setup
import cyrlcd

setup(
    name='cyrlcd',
    version=cyrlcd.__version__,
    description=cyrlcd.__doc__.strip(),
    packages=['cyrlcd'],
    author=cyrlcd.__author__,
    author_email='stgolovanov@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities'
        ]
)

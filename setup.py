#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='mt',
    version='0.0.1',
    author='Dmitry Misharov',
    # install_requires=[
    #     'cached_property',
    #     'navmazing',
    #     'pytest',
    #     'taretto',
    #     'wait_for',
    #     'widgetastic.core',
    #     'widgetastic.bootstrap'
    # ],
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license='GNU GPL v3.0',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ),
)
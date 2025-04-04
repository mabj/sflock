# Copyright (C) 2015-2018 Jurriaan Bremer.
# Copyright (C) 2018-2019 Hatching B.V.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from setuptools import setup

setup(
    name="SFlock",
    version="1.0",
    author="Hatching B.V.",
    author_email="jbr@hatching.io",
    packages=[
        "sflock",
        "sflock.unpack",
        "sflock.data",
    ],
    entry_points={
        "console_scripts": [
            "sflock = sflock.main:main",
        ],
    },
    url="http://sflock.org/",
    license="GPLv3",
    description="Sample staging and detonation utility",
    include_package_data=True,
    python_requires='>3.6',
    install_requires=[
        "click==7.0",
        "cryptography>=3.2",
        "olefile>=0.43,<0.50",
        "peepdf>=0.4.1,<0.5",
        "python-magic>=0.4,<0.5",
    ],
    extras_require={
        'test': ['pytest', 'mock']
    }
)

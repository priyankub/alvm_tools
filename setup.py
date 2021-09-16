#!/usr/bin/env python

from setuptools import setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "alvm>=0.9.2",
]

dev_dependencies = [
    "pytest",
]

setup(
    name="alvm_tools",
    version="0.4.3",
    packages=["ir", "alvm_tools", "alvm_tools.setuptools", "stages", "stages.stage_2",],
    author="Sten Achiho",
    entry_points={
        "console_scripts": [
            "read_ir = alvm_tools.cmds:read_ir",
            "opc = alvm_tools.cmds:opc",
            "opd = alvm_tools.cmds:opd",
            "run = alvm_tools.cmds:run",
            "brun = alvm_tools.cmds:brun",
        ],
    },
    author_email="sten@achicoin.org",
    #setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    #use_scm_version={"fallback_version": "unknown"},
    url="https://github.com/Achi-Coin",
    license="https://opensource.org/licenses/Apache-2.0",
    description="ALVM compiler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(dev=dev_dependencies,),
    project_urls={
        "Bug Reports": "https://github.com/Achi-Coin/alvm_tools",
        "Source": "https://github.com/Achi-Coin/alvm_tools",
    },
)

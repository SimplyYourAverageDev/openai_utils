from setuptools import setup, find_packages

import os

VERSION = '2.5'

DESCRIPTION = "Some external utilities to facilitate OpenAI's Utilites"

with open("README.md", 'r') as r:

    long_description = r.read()

# Setting up

setup(
    name="openai-utilties",
    version=VERSION,
    author="YourAverageDev",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["openai"],  # Libaries needed to run your libary correctly
    keywords=['openai', 'utilities'],  # Keywords for search on Pypi
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license="MIT"  # The kind of License needed for your Libary
)


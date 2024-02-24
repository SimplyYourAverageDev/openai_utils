from setuptools import setup, find_packages

VERSION = '3.5'
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
   install_requires=["openai>=1.2.3"], # Libraries needed to run your library correctly
   keywords=['openai', 'utilities'], # Keywords for search on PyPI
   classifiers=[
       "Development Status :: 5 - Production/Stable",
       "Intended Audience :: Developers",
       "Programming Language :: Python :: 3.9", # Added Python 3.9
       "Programming Language :: Python :: 3.10", # Added Python 3.10
       "Programming Language :: Python :: 3.11", # Added Python 3.11
       "Programming Language :: Python :: 3.12", # Added Python 3.12
       "Operating System :: Unix",
       "Operating System :: MacOS :: MacOS X",
       "Operating System :: Microsoft :: Windows",
   ],
   license="MIT", # The kind of License needed for your Library
   url="https://github.com/SimplyYourAverageDev/openai_utils" # Link to your GitHub page
)

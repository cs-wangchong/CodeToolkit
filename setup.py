#!/usr/bin/env python3

import os
from   os import path
from   setuptools import setup, find_packages
import sys

print(find_packages())

reqs = [
    'numpy',
    'gensim',
    'nltk',
    'textdistance[extras]'
]

# The following reads the variables without doing an "import spiral",
# because the latter will cause the python execution environment to fail if
# any dependencies are not already installed -- negating most of the reason
# we're using setup() in the first place.  This code avoids eval, for security.

version = {}
with open('codetoolkit/__version__.py') as f:
    text = f.read().rstrip().splitlines()
    vars = [line for line in text if line.startswith('__') and '=' in line]
    for v in vars:
        setting = v.split('=')
        version[setting[0].strip()] = setting[1].strip().replace("'", '')

# Finally, define our namesake.

setup(
    name                 = version['__title__'].lower(),
    description          = version['__description__'],
    long_description     = 'The toolkit provides methods for processing source code.',
    version              = version['__version__'],
    # url                  = version['__url__'],
    # author               = version['__author__'],
    # author_email         = version['__email__'],
    license              = version['__license__'],
    keywords             = "program-comprehension code-processing",
    packages             = find_packages(),
    package_dir          = {
                                'codetoolkit': 'codetoolkit',
                                'codetoolkit.spiral': 'codetoolkit/spiral',
                                'codetoolkit.posse': 'codetoolkit/posse',
                            },
    package_data         = {
                                'codetoolkit': ['predicates.txt', 'verb.txt'],
                                'codetoolkit.spiral': ['data/*'],
                                'codetoolkit.posse': ['corpus/*', 'dicts/*']
                            },
    # include_package_data = True,
    install_requires     = reqs,
    platforms            = 'any',
    python_requires  = '>=3.6',
)

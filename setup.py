#!/usr/bin/env python -O

version = {
    "__version__"     : '0.2.8',
    "__title__"       : 'CodeToolkit',
    "__description__" : 'A toolkit for processing source code',
    "__license__"     : 'GNU General Public License, version 3.0',
}

import os
from   os import path
from   setuptools import setup, find_packages
import sys

reqs = [
    'six',
    'numpy',
    'gensim',
    'nltk',
    'textdistance[extras]',
    'jpype1',
    'spacy'
]

# The following reads the variables without doing an "import spiral",
# because the latter will cause the python execution environment to fail if
# any dependencies are not already installed -- negating most of the reason
# we're using setup() in the first place.  This code avoids eval, for security.

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
                                'codetoolkit': [
                                    'predicates.txt',
                                    'verb.txt',
                                    'JavaAnalysis-1.0-SNAPSHOT.jar'
                                ],
                                'codetoolkit.spiral': ['data/*'],
                                'codetoolkit.posse': ['corpus/*', 'dicts/*']
                            },
    include_package_data = True,
    install_requires     = reqs,
    platforms            = 'any',
    python_requires  = '>=3.6',
)

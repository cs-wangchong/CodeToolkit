#!/usr/bin/env python -O

version = {
    "__version__"     : '0.1.2',
    "__title__"       : 'SrcToolkit',
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
                                'srctoolkit': 'srctoolkit',
                                'srctoolkit.spiral': 'srctoolkit/spiral',
                                'srctoolkit.posse': 'srctoolkit/posse',
                            },
    package_data         = {
                                'srctoolkit': [
                                    'predicates.txt',
                                    'verb.txt',
                                    'JavaAnalysis-1.0-SNAPSHOT.jar'
                                ],
                                'srctoolkit.spiral': ['data/*'],
                                'srctoolkit.posse': ['corpus/*', 'dicts/*']
                            },
    include_package_data = True,
    install_requires     = reqs,
    platforms            = 'any',
    python_requires  = '>=3.6',
)

"""
molecool
A python package for the MSF 2020 Bootcamp
"""

# Add imports here
from .functions import *
from .atomdata import atomic weights,atom_colors

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# encoding: utf-8
# module pandas._libs.lib
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/lib.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import sys as sys # <module 'sys' (built-in)>
import pandas._libs.tslib as tslib # /usr/local/lib/python3.6/site-packages/pandas/_libs/tslib.cpython-36m-darwin.so
import pandas._libs.interval as interval # /usr/local/lib/python3.6/site-packages/pandas/_libs/interval.cpython-36m-darwin.so
from pandas._libs.interval import Interval

from pandas._libs.tslib import NaT, Timedelta, Timestamp

import datetime as __datetime
import distutils.version as __distutils_version


class LooseVersion(__distutils_version.Version):
    """
    Version numbering for anarchists and software realists.
        Implements the standard interface for version number classes as
        described above.  A version number consists of a series of numbers,
        separated by either periods or strings of letters.  When comparing
        version numbers, the numeric components will be compared
        numerically, and the alphabetic components lexically.  The following
        are all valid version numbers, in no particular order:
    
            1.5.1
            1.5.2b2
            161
            3.10a
            8.02
            3.4j
            1996.07.12
            3.2.pl0
            3.1.1.6
            2g6
            11g
            0.960923
            2.2beta29
            1.13++
            5.5.kw
            2.0b1pl0
    
        In fact, there is no such thing as an invalid version number under
        this scheme; the rules for comparison are simple and predictable,
        but may not always give the results you want (for some definition
        of "want").
    """
    def parse(self, vstring): # reliably restored by inspect
        # no doc
        pass

    def _cmp(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, vstring=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    component_re = None # (!) real value is ''



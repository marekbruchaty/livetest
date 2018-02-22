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


from .object import object

class SeriesGrouper(object):
    """
    Performs generic grouping operation while avoiding ndarray construction
        overhead
    """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ityp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default




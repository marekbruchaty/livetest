# encoding: utf-8
# module pandas._libs.tslibs.frequencies
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/tslibs/frequencies.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/re.py
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py

# Variables with simple values

_INVALID_FREQ_ERROR = 'Invalid frequency: {0}'

# functions

def get_freq_code(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return freq str or tuple to freq code and stride (mult)
    
        Parameters
        ----------
        freqstr : str or tuple
    
        Returns
        -------
        return : tuple of base frequency code and stride (mult)
    
        Example
        -------
        >>> get_freq_code('3D')
        (6000, 3)
    
        >>> get_freq_code('D')
        (6000, 1)
    
        >>> get_freq_code(('D', 3))
        (6000, 3)
    """
    pass

def _base_and_stride(*args, **kwargs): # real signature unknown
    """
    Return base freq and stride info from string representation
    
        Examples
        --------
        _freq_and_stride('5Min') -> 'Min', 5
    """
    pass

def _period_str_to_code(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

opattern = None # (!) real value is ''

_dont_uppercase = None # (!) real value is ''

_lite_rule_alias = {
    'A': 'A-DEC',
    'AS': 'AS-JAN',
    'BA': 'BA-DEC',
    'BAS': 'BAS-JAN',
    'BY': 'BA-DEC',
    'BYS': 'BAS-JAN',
    'Min': 'T',
    'Q': 'Q-DEC',
    'W': 'W-SUN',
    'Y': 'A-DEC',
    'YS': 'AS-JAN',
    'min': 'T',
    'ms': 'L',
    'ns': 'N',
    'us': 'U',
}

_period_code_map = {
    'A': 1000,
    'A-APR': 1004,
    'A-AUG': 1008,
    'A-DEC': 1000,
    'A-FEB': 1002,
    'A-JAN': 1001,
    'A-JUL': 1007,
    'A-JUN': 1006,
    'A-MAR': 1003,
    'A-MAY': 1005,
    'A-NOV': 1011,
    'A-OCT': 1010,
    'A-SEP': 1009,
    'B': 5000,
    'C': 5000,
    'D': 6000,
    'H': 7000,
    'L': 10000,
    'M': 3000,
    'N': 12000,
    'Q': 2000,
    'Q-APR': 2004,
    'Q-AUG': 2008,
    'Q-DEC': 2000,
    'Q-FEB': 2002,
    'Q-JAN': 2001,
    'Q-JUL': 2007,
    'Q-JUN': 2006,
    'Q-MAR': 2003,
    'Q-MAY': 2005,
    'Q-NOV': 2011,
    'Q-OCT': 2010,
    'Q-SEP': 2009,
    'S': 9000,
    'T': 8000,
    'U': 11000,
    'W': 4000,
    'W-FRI': 4005,
    'W-MON': 4001,
    'W-SAT': 4006,
    'W-SUN': 4000,
    'W-THU': 4004,
    'W-TUE': 4002,
    'W-WED': 4003,
    'Y-APR': 1004,
    'Y-AUG': 1008,
    'Y-DEC': 1000,
    'Y-FEB': 1002,
    'Y-JAN': 1001,
    'Y-JUL': 1007,
    'Y-JUN': 1006,
    'Y-MAR': 1003,
    'Y-MAY': 1005,
    'Y-NOV': 1011,
    'Y-OCT': 1010,
    'Y-SEP': 1009,
}

_reverse_period_code_map = {
    1000: 'A-DEC',
    1001: 'A-JAN',
    1002: 'A-FEB',
    1003: 'A-MAR',
    1004: 'A-APR',
    1005: 'A-MAY',
    1006: 'A-JUN',
    1007: 'A-JUL',
    1008: 'A-AUG',
    1009: 'A-SEP',
    1010: 'A-OCT',
    1011: 'A-NOV',
    2000: 'Q-DEC',
    2001: 'Q-JAN',
    2002: 'Q-FEB',
    2003: 'Q-MAR',
    2004: 'Q-APR',
    2005: 'Q-MAY',
    2006: 'Q-JUN',
    2007: 'Q-JUL',
    2008: 'Q-AUG',
    2009: 'Q-SEP',
    2010: 'Q-OCT',
    2011: 'Q-NOV',
    3000: 'M',
    4000: 'W-SUN',
    4001: 'W-MON',
    4002: 'W-TUE',
    4003: 'W-WED',
    4004: 'W-THU',
    4005: 'W-FRI',
    4006: 'W-SAT',
    5000: 'B',
    6000: 'D',
    7000: 'H',
    8000: 'T',
    9000: 'S',
    10000: 'L',
    11000: 'U',
    12000: 'N',
}

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'get_freq_code': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    'get_freq_code (line 14)': "\n    Return freq str or tuple to freq code and stride (mult)\n\n    Parameters\n    ----------\n    freqstr : str or tuple\n\n    Returns\n    -------\n    return : tuple of base frequency code and stride (mult)\n\n    Example\n    -------\n    >>> get_freq_code('3D')\n    (6000, 3)\n\n    >>> get_freq_code('D')\n    (6000, 1)\n\n    >>> get_freq_code(('D', 3))\n    (6000, 3)\n    ",
}


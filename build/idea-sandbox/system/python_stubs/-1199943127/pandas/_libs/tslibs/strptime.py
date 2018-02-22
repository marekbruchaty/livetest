# encoding: utf-8
# module pandas._libs.tslibs.strptime
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/tslibs/strptime.cpython-36m-darwin.so
# by generator 1.145
""" Strptime-related classes and functions. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import time as time # <module 'time' (built-in)>
import locale as locale # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/locale.py
import calendar as calendar # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/calendar.py
import re as re # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/re.py
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
from _thread import _thread_allocate_lock


# Variables with simple values

_CACHE_MAX_SIZE = 5

# functions

def array_strptime(*args, **kwargs): # real signature unknown
    """
    Calculates the datetime structs represented by the passed array of strings
    
        Parameters
        ----------
        values : ndarray of string-like objects
        fmt : string-like regex
        exact : matches must be exact if True, search if False
        coerce : if invalid values found, coerce to NaT
    """
    pass

def _getlang(*args, **kwargs): # real signature unknown
    """ Figure out what language is being used for the locale """
    pass

# classes

class datetime_date(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp -> local date from a POSIX timestamp (like time.time()). """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


class LocaleTime(object):
    """
    Stores and handles locale-specific information related to time.
    
        ATTRIBUTES:
            f_weekday -- full weekday names (7-item list)
            a_weekday -- abbreviated weekday names (7-item list)
            f_month -- full month names (13-item list; dummy value in [0], which
                        is added by code)
            a_month -- abbreviated month names (13-item list, dummy value in
                        [0], which is added by code)
            am_pm -- AM/PM representation (2-item list)
            LC_date_time -- format string for date/time representation (string)
            LC_date -- format string for date representation (string)
            LC_time -- format string for time representation (string)
            timezone -- daylight- and non-daylight-savings timezone representation
                        (2-item list of sets)
            lang -- Language used by instance (2-item tuple)
    """
    def _LocaleTime__calc_am_pm(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_date_time(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_month(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_timezone(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_weekday(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__pad(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Set all attributes.
        
                Order of methods called matters for dependency reasons.
        
                The locale language is set at the offset and then checked again before
                exiting.  This is to make sure that the attributes were not set with a
                mix of information from more than one locale.  This would most likely
                happen when using threads where one thread calls a locale-dependent
                function while another thread changes the locale while the function in
                the other thread is still running.  Proper coding would call for
                locks to prevent changing the locale while locale-dependent code is
                running.  The check here is done in case someone does not think about
                doing this.
        
                Only other possible issue is if someone changed the timezone and did
                not call tz.tzset .  That is an issue for the programmer, though,
                since changing the timezone is worthless without that call.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class TimeRE(dict):
    """
    Handle conversion from format directives to regexes.
    
        Creates regexes for pattern matching a string of text containing
        time information
    """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Return a compiled re object for the format string. """
        pass

    def pattern(self, *args, **kwargs): # real signature unknown
        """
        Return regex pattern for the format string.
        
                Need to make sure that any characters that might be interpreted as
                regex syntax are escaped.
        """
        pass

    def _TimeRE__seqToRE(self, *args, **kwargs): # real signature unknown
        """
        Convert a list to a regex string for matching a directive.
        
                Want possible matching values to be from longest to shortest.  This
                prevents the possibility of a match occuring for a value that also
                a substring of a larger value that should have matched (e.g., 'abc'
                matching when 'abcdef' should have been the match).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create keys/values.
        
                Order of execution is important for dependency reasons.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

_cache_lock = None # (!) real value is ''

_regex_cache = {}

_TimeRE_cache = {
    '%': '%',
    'A': '(?P<A>wednesday|thursday|saturday|tuesday|monday|friday|sunday)',
    'B': '(?P<B>september|february|november|december|january|october|august|march|april|june|july|may)',
    'H': '(?P<H>2[0-3]|[0-1]\\d|\\d)',
    'I': '(?P<I>1[0-2]|0[1-9]|[1-9])',
    'M': '(?P<M>[0-5]\\d|\\d)',
    'S': '(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'U': '(?P<U>5[0-3]|[0-4]\\d|\\d)',
    'W': '(?P<W>5[0-3]|[0-4]\\d|\\d)',
    'X': '(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'Y': '(?P<Y>\\d\\d\\d\\d)',
    'Z': '(?P<Z>cest|gmt|cet|utc)',
    'a': '(?P<a>mon|tue|wed|thu|fri|sat|sun)',
    'b': '(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
    'c': '(?P<a>mon|tue|wed|thu|fri|sat|sun)\\s+(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\\s+(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])\\s+(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)\\s+(?P<Y>\\d\\d\\d\\d)',
    'd': '(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])',
    'f': '(?P<f>[0-9]{1,9})',
    'j': '(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])',
    'm': '(?P<m>1[0-2]|0[1-9]|[1-9])',
    'p': '(?P<p>am|pm)',
    'w': '(?P<w>[0-6])',
    'x': '(?P<m>1[0-2]|0[1-9]|[1-9])/(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])/(?P<y>\\d\\d)',
    'y': '(?P<y>\\d\\d)',
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}


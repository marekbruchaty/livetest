# encoding: utf-8
# module pandas._libs.tslibs.timezones
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/tslibs/timezones.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pytz as pytz # /usr/local/lib/python3.6/site-packages/pytz/__init__.py
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import datetime as __datetime
import dateutil.tz._common as __dateutil_tz__common


# functions

def dateutil_gettz(name=None): # reliably restored by inspect
    # no doc
    pass

def get_timezone(*args, **kwargs): # real signature unknown
    """
    We need to do several things here:
        1) Distinguish between pytz and dateutil timezones
        2) Not be over-specific (e.g. US/Eastern with/without DST is same *zone*
           but a different tz object)
        3) Provide something to serialize when we're storing a datetime object
           in pytables.
    
        We return a string prefaced with dateutil if it's a dateutil tz, else just
        the tz name. It needs to be a string so that we can serialize it with
        UJSON/pytables. maybe_get_tz (below) is the inverse of this process.
    """
    pass

def get_utcoffset(*args, **kwargs): # real signature unknown
    pass

def infer_tzinfo(*args, **kwargs): # real signature unknown
    pass

def maybe_get_tz(*args, **kwargs): # real signature unknown
    """
    (Maybe) Construct a timezone object from a string. If tz is a string, use
        it to construct a timezone object. Otherwise, just return tz.
    """
    pass

def unbox_utcoffsets(*args, **kwargs): # real signature unknown
    pass

def _p_tz_cache_key(*args, **kwargs): # real signature unknown
    """ Python interface for cache function to facilitate testing. """
    pass

# classes

class _dateutil_tzfile(__dateutil_tz__common._tzinfo):
    """
    This is a ``tzinfo`` subclass thant allows one to use the ``tzfile(5)``
        format timezone files to extract current and historical zone information.
    
        :param fileobj:
            This can be an opened file stream or a file name that the time zone
            information can be read from.
    
        :param filename:
            This is an optional parameter specifying the source of the time zone
            information in the event that ``fileobj`` is a file object. If omitted
            and ``fileobj`` is a file stream, this parameter will be set either to
            ``fileobj``'s ``name`` attribute or to ``repr(fileobj)``.
    
        See `Sources for Time Zone and Daylight Saving Time Data
        <http://www.twinsun.com/tz/tz-link.htm>`_ for more information. Time zone
        files can be compiled from the `IANA Time Zone database files
        <https://www.iana.org/time-zones>`_ with the `zic time zone compiler
        <https://www.freebsd.org/cgi/man.cgi?query=zic&sektion=8>`_
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        The ``tzfile`` implementation of :py:func:`datetime.tzinfo.fromutc`.
        
                :param dt:
                    A :py:class:`datetime.datetime` object.
        
                :raises TypeError:
                    Raised if ``dt`` is not a :py:class:`datetime.datetime` object.
        
                :raises ValueError:
                    Raised if this is called with a ``dt`` which does not have this
                    ``tzinfo`` attached.
        
                :return:
                    Returns a :py:class:`datetime.datetime` object representing the
                    wall time in ``self``'s time zone.
        """
        pass

    def is_ambiguous(self, dt, idx=None): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _find_last_transition(self, dt, in_utc=False): # reliably restored by inspect
        # no doc
        pass

    def _find_ttinfo(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _get_ttinfo(self, idx): # reliably restored by inspect
        # no doc
        pass

    def _read_tzfile(self, fileobj): # reliably restored by inspect
        # no doc
        pass

    def _resolve_ambiguous_time(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _set_tzdata(self, tzobj): # reliably restored by inspect
        """ Set the time zone data of this object from a _tzfile object """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, fileobj, filename=None): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, protocol): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __hash__ = None


class _dateutil_tzlocal(__dateutil_tz__common._tzinfo):
    """ A :class:`tzinfo` subclass built around the ``time`` timezone functions. """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _isdst(self, dt, fold_naive=True): # reliably restored by inspect
        # no doc
        pass

    def _naive_is_dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __hash__ = None


class _dateutil_tzutc(__datetime.tzinfo):
    """ This is a tzinfo object that represents the UTC time zone. """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __hash__ = None


class _pytz_BaseTzInfo(__datetime.tzinfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    zone = None
    _tzname = None
    _utcoffset = None
    __dict__ = None # (!) real value is ''


# variables with complex values

dst_cache = {}

UTC = pytz.UTC

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'get_dst_info': None, # (!) real value is ''
    'get_timezone': None, # (!) real value is ''
    'get_utcoffset': None, # (!) real value is ''
    'is_fixed_offset': None, # (!) real value is ''
    'is_tzlocal': None, # (!) real value is ''
    'is_utc': None, # (!) real value is ''
    'maybe_get_tz': None, # (!) real value is ''
    'treat_tz_as_dateutil': None, # (!) real value is ''
    'treat_tz_as_pytz': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}


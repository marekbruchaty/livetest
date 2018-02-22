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


# Variables with simple values

iNaT = -9223372036854775808

is_numpy_prior_1_6_2 = False

# functions

def apply_frame_axis0(*args, **kwargs): # real signature unknown
    pass

def array_equivalent_object(*args, **kwargs): # real signature unknown
    """
    perform an element by element comparion on 1-d object arrays
            taking into account nan positions
    """
    pass

def arrmap(*args, **kwargs): # real signature unknown
    pass

def astype_intsafe(*args, **kwargs): # real signature unknown
    pass

def astype_str(*args, **kwargs): # real signature unknown
    pass

def astype_unicode(*args, **kwargs): # real signature unknown
    pass

def checknull(*args, **kwargs): # real signature unknown
    pass

def checknull_old(*args, **kwargs): # real signature unknown
    pass

def clean_index_list(*args, **kwargs): # real signature unknown
    """ Utility used in pandas.core.index._ensure_index """
    pass

def convert_json_to_lines(*args, **kwargs): # real signature unknown
    """
    replace comma separated json with line feeds, paying special attention
        to quotes & brackets
    """
    pass

def convert_sql_column(*args, **kwargs): # real signature unknown
    pass

def convert_timestamps(*args, **kwargs): # real signature unknown
    pass

def count_level_2d(*args, **kwargs): # real signature unknown
    pass

def dicts_to_array(*args, **kwargs): # real signature unknown
    pass

def downcast_int64(*args, **kwargs): # real signature unknown
    pass

def fast_multiget(*args, **kwargs): # real signature unknown
    pass

def fast_unique(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list_gen(*args, **kwargs): # real signature unknown
    """
    Generate a list of unique values from a generator of lists.
    
        Parameters
        ----------
        gen : generator object
            A generator of lists from which the unique list is created
        sort : boolean
            Whether or not to sort the resulting unique list
    
        Returns
        -------
        unique_list : list of unique values
    """
    pass

def fast_zip(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def fast_zip_fillna(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def generate_bins_dt64(*args, **kwargs): # real signature unknown
    """ Int64 (datetime64) version of generic python version in groupby.py """
    pass

def generate_slices(*args, **kwargs): # real signature unknown
    pass

def get_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Enumerate contiguous runs of integers in ndarray.
    
        Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``
        pairs for each contiguous run found.
    
        If `group` is True and there is more than one run for a certain blkno,
        ``(blkno, array)`` with an array containing positions of all elements equal
        to blkno.
    
        Returns
        -------
        iter : iterator of (int, slice or array)
    """
    pass

def get_level_sorter(*args, **kwargs): # real signature unknown
    """
    argsort for a single level of a multi-index, keeping the order of higher
        levels unchanged. `starts` points to starts of same-key indices w.r.t
        to leading levels; equivalent to:
            np.hstack([label[starts[i]:starts[i+1]].argsort(kind='mergesort')
                + starts[i] for i in range(len(starts) - 1)])
    """
    pass

def get_reverse_indexer(*args, **kwargs): # real signature unknown
    """
    Reverse indexing operation.
    
        Given `indexer`, make `indexer_inv` of it, such that::
    
            indexer_inv[indexer[x]] = x
    
        .. note:: If indexer is not unique, only first occurrence is accounted.
    """
    pass

def group_count(*args, **kwargs): # real signature unknown
    pass

def has_infs_f4(*args, **kwargs): # real signature unknown
    pass

def has_infs_f8(*args, **kwargs): # real signature unknown
    pass

def indexer_as_slice(*args, **kwargs): # real signature unknown
    pass

def indices_fast(*args, **kwargs): # real signature unknown
    pass

def infer_datetimelike_array(*args, **kwargs): # real signature unknown
    """
    infer if we have a datetime or timedelta array
        - date: we have *only* date and maybe strings, nulls
        - datetime: we have *only* datetimes and maybe strings, nulls
        - timedelta: we have *only* timedeltas and maybe strings, nulls
        - nat: we do not have *any* date, datetimes or timedeltas, but do have
          at least a NaT
        - mixed: other objects (strings or actual objects)
    
        Parameters
        ----------
        arr : object array
    
        Returns
        -------
        string: {datetime, timedelta, date, nat, mixed}
    """
    pass

def infer_dtype(foo=None, bar=None): # real signature unknown; restored from __doc__
    """
    Efficiently infer the type of a passed val, or list-like
        array of values. Return a string describing the type.
    
        Parameters
        ----------
        value : scalar, list, ndarray, or pandas type
        skipna : bool, default False
            Ignore NaN values when inferring the type. The default of ``False``
            will be deprecated in a later version of pandas.
    
            .. versionadded:: 0.21.0
    
        Returns
        -------
        string describing the common type of the input data.
        Results can include:
    
        - string
        - unicode
        - bytes
        - floating
        - integer
        - mixed-integer
        - mixed-integer-float
        - decimal
        - complex
        - categorical
        - boolean
        - datetime64
        - datetime
        - date
        - timedelta64
        - timedelta
        - time
        - period
        - mixed
    
        Raises
        ------
        TypeError if ndarray-like but cannot infer the dtype
    
        Notes
        -----
        - 'mixed' is the catchall for anything that is not otherwise
          specialized
        - 'mixed-integer-float' are floats and integers
        - 'mixed-integer' are integers mixed with non-integers
    
        Examples
        --------
        >>> infer_dtype(['foo', 'bar'])
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=True)
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=False)
        'mixed'
    
        >>> infer_dtype([b'foo', b'bar'])
        'bytes'
    
        >>> infer_dtype([1, 2, 3])
        'integer'
    
        >>> infer_dtype([1, 2, 3.5])
        'mixed-integer-float'
    
        >>> infer_dtype([1.0, 2.0, 3.5])
        'floating'
    
        >>> infer_dtype(['a', 1])
        'mixed-integer'
    
        >>> infer_dtype([Decimal(1), Decimal(2.0)])
        'decimal'
    
        >>> infer_dtype([True, False])
        'boolean'
    
        >>> infer_dtype([True, False, np.nan])
        'mixed'
    
        >>> infer_dtype([pd.Timestamp('20130101')])
        'datetime'
    
        >>> infer_dtype([datetime.date(2013, 1, 1)])
        'date'
    
        >>> infer_dtype([np.datetime64('2013-01-01')])
        'datetime64'
    
        >>> infer_dtype([datetime.timedelta(0, 1, 1)])
        'timedelta'
    
        >>> infer_dtype(pd.Series(list('aabc')).astype('category'))
        'categorical'
    """
    pass

def isnan(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Test element-wise for NaN and return result as a boolean array.
    
    Parameters
    ----------
    x : array_like
        Input array.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or `None`,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        Values of True indicate to calculate the ufunc at that position, values
        of False indicate to leave the value in the output alone.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.
    
    Returns
    -------
    y : ndarray or bool
        For scalar input, the result is a new boolean with value True if
        the input is NaN; otherwise the value is False.
    
        For array input, the result is a boolean array of the same
        dimensions as the input and the values are True if the
        corresponding element of the input is NaN; otherwise the values are
        False.
    
    See Also
    --------
    isinf, isneginf, isposinf, isfinite, isnat
    
    Notes
    -----
    NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754). This means that Not a Number is not equivalent to infinity.
    
    Examples
    --------
    >>> np.isnan(np.nan)
    True
    >>> np.isnan(np.inf)
    False
    >>> np.isnan([np.log(-1.),1.,np.log(0)])
    array([ True, False, False], dtype=bool)
    """
    pass

def isnaobj(*args, **kwargs): # real signature unknown
    pass

def isnaobj2d(*args, **kwargs): # real signature unknown
    pass

def isnaobj2d_old(*args, **kwargs): # real signature unknown
    pass

def isnaobj_old(*args, **kwargs): # real signature unknown
    pass

def isneginf_scalar(*args, **kwargs): # real signature unknown
    pass

def isposinf_scalar(*args, **kwargs): # real signature unknown
    pass

def isscalar(*args, **kwargs): # real signature unknown
    """
    Return True if given value is scalar.
    
        This includes:
        - numpy array scalar (e.g. np.int64)
        - Python builtin numerics
        - Python builtin byte arrays and strings
        - None
        - instances of datetime.datetime
        - instances of datetime.timedelta
        - Period
        - instances of decimal.Decimal
        - Interval
    """
    pass

def is_bool(*args, **kwargs): # real signature unknown
    pass

def is_bool_array(*args, **kwargs): # real signature unknown
    pass

def is_bytes_array(*args, **kwargs): # real signature unknown
    pass

def is_complex(*args, **kwargs): # real signature unknown
    pass

def is_datetime64_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_with_singletz_array(*args, **kwargs): # real signature unknown
    """
    Check values have the same tzinfo attribute.
        Doesn't check values are datetime-like types.
    """
    pass

def is_date_array(*args, **kwargs): # real signature unknown
    pass

def is_decimal(*args, **kwargs): # real signature unknown
    pass

def is_float(*args, **kwargs): # real signature unknown
    pass

def is_float_array(*args, **kwargs): # real signature unknown
    pass

def is_integer(*args, **kwargs): # real signature unknown
    pass

def is_integer_array(*args, **kwargs): # real signature unknown
    pass

def is_integer_float_array(*args, **kwargs): # real signature unknown
    pass

def is_interval(*args, **kwargs): # real signature unknown
    pass

def is_interval_array(*args, **kwargs): # real signature unknown
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_period(*args, **kwargs): # real signature unknown
    """ Return a boolean if this is a Period object """
    pass

def is_period_array(*args, **kwargs): # real signature unknown
    pass

def is_string_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta64_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_or_timedelta64_array(*args, **kwargs): # real signature unknown
    """ infer with timedeltas and/or nat/none """
    pass

def is_time_array(*args, **kwargs): # real signature unknown
    pass

def is_unicode_array(*args, **kwargs): # real signature unknown
    pass

def item_from_zerodim(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    If the value is a zerodim array, return the item it contains.
    
        Examples
        --------
        >>> item_from_zerodim(1)
        1
        >>> item_from_zerodim('foobar')
        'foobar'
        >>> item_from_zerodim(np.array(1))
        1
        >>> item_from_zerodim(np.array([1]))
        array([1])
    """
    pass

def list_to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert list to object ndarray. Seriously can't believe
        I had to write this function.
    """
    pass

def lookup_values(*args, **kwargs): # real signature unknown
    pass

def map_indices_list(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_infer(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def map_infer_mask(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def max_len_string_array(*args, **kwargs): # real signature unknown
    """ return the maximum size of elements in a 1-dim string array """
    pass

def maybe_booleans_to_slice(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_numeric(*args, **kwargs): # real signature unknown
    """
    Convert object array to a numeric array if possible.
    
        Parameters
        ----------
        values : ndarray
            Array of object elements to convert.
        na_values : set
            Set of values that should be interpreted as NaN.
        convert_empty : bool, default True
            If an empty array-like object is encountered, whether to interpret
            that element as NaN or not. If set to False, a ValueError will be
            raised if such an element is encountered and 'coerce_numeric' is False.
        coerce_numeric : bool, default False
            If initial attempts to convert to numeric have failed, whether to
            force conversion to numeric via alternative methods or by setting the
            element to NaN. Otherwise, an Exception will be raised when such an
            element is encountered.
    
            This boolean also has an impact on how conversion behaves when a
            numeric array has no suitable numerical dtype to return (i.e. uint64,
            int32, uint8). If set to False, the original object array will be
            returned. Otherwise, a ValueError will be raised.
    
        Returns
        -------
        numeric_array : array of converted object values to numerical ones
    """
    pass

def maybe_convert_objects(*args, **kwargs): # real signature unknown
    """ Type inference function-- convert object array to proper dtype """
    pass

def maybe_indices_to_slice(*args, **kwargs): # real signature unknown
    pass

def memory_usage_of_objects(*args, **kwargs): # real signature unknown
    """
    return the memory usage of an object array in bytes,
        does not include the actual bytes of the pointers
    """
    pass

def reduce(*args, **kwargs): # real signature unknown
    """
    Parameters
        -----------
        arr : NDFrame object
        f : function
        axis : integer axis
        dummy : type of reduced output (series)
        labels : Index or None
    """
    pass

def row_bool_subset(*args, **kwargs): # real signature unknown
    pass

def row_bool_subset_object(*args, **kwargs): # real signature unknown
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    pass

def slice_canonize(*args, **kwargs): # real signature unknown
    """ Convert slice to canonical bounded form. """
    pass

def slice_getitem(*args, **kwargs): # real signature unknown
    pass

def slice_get_indices_ex(*args, **kwargs): # real signature unknown
    """
    Get (start, stop, step, length) tuple for a slice.
    
        If `objlen` is not specified, slice must be bounded, otherwise the result
        will be wrong.
    """
    pass

def slice_len(*args, **kwargs): # real signature unknown
    """
    Get length of a bounded slice.
    
        The slice must not have any "open" bounds that would create dependency on
        container size, i.e.:
        - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``
        - if ``s.step < 0``, ``s.start`` is not ``None``
    
        Otherwise, the result is unreliable.
    """
    pass

def string_array_replace_from_nan_rep(*args, **kwargs): # real signature unknown
    """
    Replace the values in the array with 'replacement' if
        they are 'nan_rep'. Return the same array.
    """
    pass

def to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert a list of lists into an object array.
    
        Parameters
        ----------
        rows : 2-d array (N, K)
            A list of lists to be converted into an array
        min_width : int
            The minimum width of the object array. If a list
            in `rows` contains fewer than `width` elements,
            the remaining elements in the corresponding row
            will all be `NaN`.
    
        Returns
        -------
        obj_array : numpy array of the object dtype
    """
    pass

def to_object_array_tuples(*args, **kwargs): # real signature unknown
    pass

def tuples_to_object_array(*args, **kwargs): # real signature unknown
    pass

def values_from_object(*args, **kwargs): # real signature unknown
    """ return my values or the object if we are say an ndarray """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    pass

def write_csv_rows(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockPlacement(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Reducer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeriesBinGrouper(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeriesGrouper(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Slider(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__PandasNull(*args, **kwargs): # real signature unknown
    pass

# classes

from .Validator import Validator
from .TemporalValidator import TemporalValidator
from .TimedeltaValidator import TimedeltaValidator
from .AnyTimedeltaValidator import AnyTimedeltaValidator
from .BlockPlacement import BlockPlacement
from .BlockSlider import BlockSlider
from .BoolValidator import BoolValidator
from .BytesValidator import BytesValidator
from .datetime import datetime
from .DatetimeValidator import DatetimeValidator
from .Datetime64Validator import Datetime64Validator
from .DateValidator import DateValidator
from .Decimal import Decimal
from .FloatValidator import FloatValidator
from .IntegerFloatValidator import IntegerFloatValidator
from .IntegerValidator import IntegerValidator
from .IntervalValidator import IntervalValidator
from .InvalidApply import InvalidApply
from .LooseVersion import LooseVersion
from .PeriodValidator import PeriodValidator
from .Reducer import Reducer
from .Seen import Seen
from .SeriesBinGrouper import SeriesBinGrouper
from .SeriesGrouper import SeriesGrouper
from .Slider import Slider
from .StringValidator import StringValidator
from .timedelta import timedelta
from .Timedelta64Validator import Timedelta64Validator
from .TimeValidator import TimeValidator
from .UnicodeValidator import UnicodeValidator
from ._PandasNull import _PandasNull
# variables with complex values

pandas_null = None # (!) real value is ''

_TYPE_MAP = {
    'M': 'datetime64',
    'S': 'bytes',
    'U': 'string',
    'b': 'boolean',
    'bool': 'boolean',
    'c': 'complex',
    'categorical': 'categorical',
    'category': 'categorical',
    'complex128': 'complex',
    'complex256': 'complex',
    'datetime64[ns]': 'datetime64',
    'f': 'floating',
    'float128': 'floating',
    'float16': 'floating',
    'float32': 'floating',
    'float64': 'floating',
    'i': 'integer',
    'int16': 'integer',
    'int32': 'integer',
    'int64': 'integer',
    'int8': 'integer',
    'm': 'timedelta64',
    'string': 'bytes',
    'timedelta64[ns]': 'timedelta64',
    'u': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'uint8': 'integer',
    'unicode': 'string',
}

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'is_null_datetimelike': None, # (!) real value is ''
    'is_period': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    'infer_dtype (line 215)': "\n    Efficiently infer the type of a passed val, or list-like\n    array of values. Return a string describing the type.\n\n    Parameters\n    ----------\n    value : scalar, list, ndarray, or pandas type\n    skipna : bool, default False\n        Ignore NaN values when inferring the type. The default of ``False``\n        will be deprecated in a later version of pandas.\n\n        .. versionadded:: 0.21.0\n\n    Returns\n    -------\n    string describing the common type of the input data.\n    Results can include:\n\n    - string\n    - unicode\n    - bytes\n    - floating\n    - integer\n    - mixed-integer\n    - mixed-integer-float\n    - decimal\n    - complex\n    - categorical\n    - boolean\n    - datetime64\n    - datetime\n    - date\n    - timedelta64\n    - timedelta\n    - time\n    - period\n    - mixed\n\n    Raises\n    ------\n    TypeError if ndarray-like but cannot infer the dtype\n\n    Notes\n    -----\n    - 'mixed' is the catchall for anything that is not otherwise\n      specialized\n    - 'mixed-integer-float' are floats and integers\n    - 'mixed-integer' are integers mixed with non-integers\n\n    Examples\n    --------\n    >>> infer_dtype(['foo', 'bar'])\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=True)\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=False)\n    'mixed'\n\n    >>> infer_dtype([b'foo', b'bar'])\n    'bytes'\n\n    >>> infer_dtype([1, 2, 3])\n    'integer'\n\n    >>> infer_dtype([1, 2, 3.5])\n    'mixed-integer-float'\n\n    >>> infer_dtype([1.0, 2.0, 3.5])\n    'floating'\n\n    >>> infer_dtype(['a', 1])\n    'mixed-integer'\n\n    >>> infer_dtype([Decimal(1), Decimal(2.0)])\n    'decimal'\n\n    >>> infer_dtype([True, False])\n    'boolean'\n\n    >>> infer_dtype([True, False, np.nan])\n    'mixed'\n\n    >>> infer_dtype([pd.Timestamp('20130101')])\n    'datetime'\n\n    >>> infer_dtype([datetime.date(2013, 1, 1)])\n    'date'\n\n    >>> infer_dtype([np.datetime64('2013-01-01')])\n    'datetime64'\n\n    >>> infer_dtype([datetime.timedelta(0, 1, 1)])\n    'timedelta'\n\n    >>> infer_dtype(pd.Series(list('aabc')).astype('category'))\n    'categorical'\n    ",
    'item_from_zerodim (line 205)': "\n    If the value is a zerodim array, return the item it contains.\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n\n    ",
}


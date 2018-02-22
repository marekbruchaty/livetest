# encoding: utf-8
# module pandas._libs.parsers
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/parsers.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/warnings.py
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import pandas._libs.lib as lib # /usr/local/lib/python3.6/site-packages/pandas/_libs/lib.cpython-36m-darwin.so
import pandas.compat as compat # /usr/local/lib/python3.6/site-packages/pandas/compat/__init__.py
import pandas.io.common as com # /usr/local/lib/python3.6/site-packages/pandas/io/common.py
import time as time # <module 'time' (built-in)>
import os as os # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py
import sys as sys # <module 'sys' (built-in)>
import numpy as __numpy
import pandas.core.base as __pandas_core_base
import pandas.core.dtypes.dtypes as __pandas_core_dtypes_dtypes


# Variables with simple values

DEFAULT_CHUNKSIZE = 262144

QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

# functions

def is_bool_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a boolean dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of a boolean dtype.
    
        Examples
        --------
        >>> is_bool_dtype(str)
        False
        >>> is_bool_dtype(int)
        False
        >>> is_bool_dtype(bool)
        True
        >>> is_bool_dtype(np.bool)
        True
        >>> is_bool_dtype(np.array(['a', 'b']))
        False
        >>> is_bool_dtype(pd.Series([1, 2]))
        False
        >>> is_bool_dtype(np.array([True, False]))
        True
    """
    pass

def is_categorical_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the Categorical dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is
                  of the Categorical dtype.
    
        Examples
        --------
        >>> is_categorical_dtype(object)
        False
        >>> is_categorical_dtype(CategoricalDtype())
        True
        >>> is_categorical_dtype([1, 2, 3])
        False
        >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))
        True
        >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))
        True
    """
    pass

def is_datetime64_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the datetime64 dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is of
                  the datetime64 dtype.
    
        Examples
        --------
        >>> is_datetime64_dtype(object)
        False
        >>> is_datetime64_dtype(np.datetime64)
        True
        >>> is_datetime64_dtype(np.array([], dtype=int))
        False
        >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
        True
        >>> is_datetime64_dtype([1, 2, 3])
        False
    """
    pass

def is_float_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a float dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of a float dtype.
    
        Examples
        --------
        >>> is_float_dtype(str)
        False
        >>> is_float_dtype(int)
        False
        >>> is_float_dtype(float)
        True
        >>> is_float_dtype(np.array(['a', 'b']))
        False
        >>> is_float_dtype(pd.Series([1, 2]))
        False
        >>> is_float_dtype(pd.Index([1, 2.]))
        True
    """
    pass

def is_integer_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of an integer dtype.
    
        Unlike in `in_any_int_dtype`, timedelta64 instances will return False.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of an integer dtype
                  and not an instance of timedelta64.
    
        Examples
        --------
        >>> is_integer_dtype(str)
        False
        >>> is_integer_dtype(int)
        True
        >>> is_integer_dtype(float)
        False
        >>> is_integer_dtype(np.uint64)
        True
        >>> is_integer_dtype(np.datetime64)
        False
        >>> is_integer_dtype(np.timedelta64)
        False
        >>> is_integer_dtype(np.array(['a', 'b']))
        False
        >>> is_integer_dtype(pd.Series([1, 2]))
        True
        >>> is_integer_dtype(np.array([], dtype=np.timedelta64))
        False
        >>> is_integer_dtype(pd.Index([1, 2.]))  # float
        False
    """
    pass

def is_object_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the object dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is of the object dtype.
    
        Examples
        --------
        >>> is_object_dtype(object)
        True
        >>> is_object_dtype(int)
        False
        >>> is_object_dtype(np.array([], dtype=object))
        True
        >>> is_object_dtype(np.array([], dtype=int))
        False
        >>> is_object_dtype([1, 2, 3])
        False
    """
    pass

def pandas_dtype(dtype): # reliably restored by inspect
    """
    Converts input into a pandas only dtype object or a numpy dtype object.
    
        Parameters
        ----------
        dtype : object to be converted
    
        Returns
        -------
        np.dtype or a pandas dtype
    """
    pass

def union_categoricals(to_union, sort_categories=False, ignore_order=False): # reliably restored by inspect
    """
    Combine list-like of Categorical-like, unioning categories. All
        categories must have the same dtype.
    
        .. versionadded:: 0.19.0
    
        Parameters
        ----------
        to_union : list-like of Categorical, CategoricalIndex,
                   or Series with dtype='category'
        sort_categories : boolean, default False
            If true, resulting categories will be lexsorted, otherwise
            they will be ordered as they appear in the data.
        ignore_order: boolean, default False
            If true, the ordered attribute of the Categoricals will be ignored.
            Results in an unordered categorical.
    
            .. versionadded:: 0.20.0
    
        Returns
        -------
        result : Categorical
    
        Raises
        ------
        TypeError
            - all inputs do not have the same dtype
            - all inputs do not have the same ordered property
            - all inputs are ordered and their categories are not identical
            - sort_categories=True and Categoricals are ordered
        ValueError
            Empty list of categoricals passed
    
        Notes
        -----
    
        To learn more about categories, see `link
        <http://pandas.pydata.org/pandas-docs/stable/categorical.html#unioning>`__
    
        Examples
        --------
    
        >>> from pandas.api.types import union_categoricals
    
        If you want to combine categoricals that do not necessarily have
        the same categories, `union_categoricals` will combine a list-like
        of categoricals. The new categories will be the union of the
        categories being combined.
    
        >>> a = pd.Categorical(["b", "c"])
        >>> b = pd.Categorical(["a", "b"])
        >>> union_categoricals([a, b])
        [b, c, a, b]
        Categories (3, object): [b, c, a]
    
        By default, the resulting categories will be ordered as they appear
        in the `categories` of the data. If you want the categories to be
        lexsorted, use `sort_categories=True` argument.
    
        >>> union_categoricals([a, b], sort_categories=True)
        [b, c, a, b]
        Categories (3, object): [a, b, c]
    
        `union_categoricals` also works with the case of combining two
        categoricals of the same categories and order information (e.g. what
        you could also `append` for).
    
        >>> a = pd.Categorical(["a", "b"], ordered=True)
        >>> b = pd.Categorical(["a", "b", "a"], ordered=True)
        >>> union_categoricals([a, b])
        [a, b, a, b, a]
        Categories (2, object): [a < b]
    
        Raises `TypeError` because the categories are ordered and not identical.
    
        >>> a = pd.Categorical(["a", "b"], ordered=True)
        >>> b = pd.Categorical(["a", "b", "c"], ordered=True)
        >>> union_categoricals([a, b])
        TypeError: to union ordered Categoricals, all categories must be the same
    
        New in version 0.20.0
    
        Ordered categoricals with different categories or orderings can be
        combined by using the `ignore_ordered=True` argument.
    
        >>> a = pd.Categorical(["a", "b", "c"], ordered=True)
        >>> b = pd.Categorical(["c", "b", "a"], ordered=True)
        >>> union_categoricals([a, b], ignore_order=True)
        [a, b, c, c, b, a]
        Categories (3, object): [a, b, c]
    
        `union_categoricals` also works with a `CategoricalIndex`, or `Series`
        containing categorical data, but note that the resulting array will
        always be a plain `Categorical`
    
        >>> a = pd.Series(["b", "c"], dtype='category')
        >>> b = pd.Series(["a", "b"], dtype='category')
        >>> union_categoricals([a, b])
        [b, c, a, b]
        Categories (3, object): [b, c, a]
    """
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _concatenate_chunks(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _is_file_like(*args, **kwargs): # real signature unknown
    pass

def _maybe_encode(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """  """
    pass

def _to_structured_array(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class basestring(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return ""

    def casefold(self): # real signature unknown; restored from __doc__
        """
        S.casefold() -> str
        
        Return a version of S suitable for caseless comparisons.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
        """
        S.encode(encoding='utf-8', errors='strict') -> bytes
        
        Encode S using the codec registered for encoding. Default encoding
        is 'utf-8'. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return b""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str
        
        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> str
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class Categorical(__pandas_core_base.PandasObject):
    """
    Represents a categorical variable in classic R / S-plus fashion
    
        `Categoricals` can only take on only a limited, and usually fixed, number
        of possible values (`categories`). In contrast to statistical categorical
        variables, a `Categorical` might have an order, but numerical operations
        (additions, divisions, ...) are not possible.
    
        All values of the `Categorical` are either in `categories` or `np.nan`.
        Assigning values outside of `categories` will raise a `ValueError`. Order
        is defined by the order of the `categories`, not lexical order of the
        values.
    
        Parameters
        ----------
        values : list-like
            The values of the categorical. If categories are given, values not in
            categories will be replaced with NaN.
        categories : Index-like (unique), optional
            The unique categories for this categorical. If not given, the
            categories are assumed to be the unique values of values.
        ordered : boolean, (default False)
            Whether or not this categorical is treated as a ordered categorical.
            If not given, the resulting categorical will not be ordered.
        dtype : CategoricalDtype
            An instance of ``CategoricalDtype`` to use for this categorical
    
            .. versionadded:: 0.21.0
    
        Attributes
        ----------
        categories : Index
            The categories of this categorical
        codes : ndarray
            The codes (integer positions, which point to the categories) of this
            categorical, read only.
        ordered : boolean
            Whether or not this Categorical is ordered.
        dtype : CategoricalDtype
            The instance of ``CategoricalDtype`` storing the ``categories``
            and ``ordered``.
    
            .. versionadded:: 0.21.0
    
        Raises
        ------
        ValueError
            If the categories do not validate.
        TypeError
            If an explicit ``ordered=True`` is given but no `categories` and the
            `values` are not sortable.
    
        Examples
        --------
        >>> pd.Categorical([1, 2, 3, 1, 2, 3])
        [1, 2, 3, 1, 2, 3]
        Categories (3, int64): [1, 2, 3]
    
        >>> pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
        [a, b, c, a, b, c]
        Categories (3, object): [a, b, c]
    
        Ordered `Categoricals` can be sorted according to the custom order
        of the categories and can have a min and max value.
    
        >>> c = pd.Categorical(['a','b','c','a','b','c'], ordered=True,
        ...                    categories=['c', 'b', 'a'])
        >>> c
        [a, b, c, a, b, c]
        Categories (3, object): [c < b < a]
        >>> c.min()
        'c'
    
        Notes
        -----
        See the `user guide
        <http://pandas.pydata.org/pandas-docs/stable/categorical.html>`_ for more.
    
        See also
        --------
        pandas.api.types.CategoricalDtype : Type for categorical data
        CategoricalIndex : An Index with an underlying ``Categorical``
    """
    def add_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Add new categories.
        
                `new_categories` will be included at the last/highest place in the
                categories and will be unused directly after this call.
        
                Raises
                ------
                ValueError
                    If the new categories include old categories or do not validate as
                    categories
        
                Parameters
                ----------
                new_categories : category or list-like of category
                   The new categories to be included.
                inplace : boolean (default: False)
                   Whether or not to add the categories inplace or return a copy of
                   this categorical with added categories.
        
                Returns
                -------
                cat : Categorical with new categories added or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def argsort(self, ascending=True, kind=None, *args, **kwargs): # reliably restored by inspect
        """
        Returns the indices that would sort the Categorical instance if
                'sort_values' was called. This function is implemented to provide
                compatibility with numpy ndarray objects.
        
                While an ordering is applied to the category values, arg-sorting
                in this context refers more to organizing and grouping together
                based on matching category values. Thus, this function can be
                called on an unordered Categorical instance unlike the functions
                'Categorical.min' and 'Categorical.max'.
        
                Returns
                -------
                argsorted : numpy array
        
                See also
                --------
                numpy.ndarray.argsort
        """
        pass

    def astype(self, dtype, copy=True): # reliably restored by inspect
        """
        Coerce this type to another dtype
        
                Parameters
                ----------
                dtype : numpy dtype or pandas type
                copy : bool, default True
                    By default, astype always returns a newly allocated object.
                    If copy is set to False and dtype is categorical, the original
                    object is returned.
        
                    .. versionadded:: 0.19.0
        """
        pass

    def as_ordered(self, inplace=False): # reliably restored by inspect
        """
        Sets the Categorical to be ordered
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to True
        """
        pass

    def as_unordered(self, inplace=False): # reliably restored by inspect
        """
        Sets the Categorical to be unordered
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to False
        """
        pass

    def check_for_ordered(self, op): # reliably restored by inspect
        """ assert that we are ordered """
        pass

    def copy(self): # reliably restored by inspect
        """ Copy constructor. """
        pass

    def describe(self): # reliably restored by inspect
        """
        Describes this Categorical
        
                Returns
                -------
                description: `DataFrame`
                    A dataframe with frequency and counts by category.
        """
        pass

    def dropna(self): # reliably restored by inspect
        """
        Return the Categorical without null values.
        
                Both missing values (-1 in .codes) and NA as a category are detected.
                NA is removed from the categories if present.
        
                Returns
                -------
                valid : Categorical
        """
        pass

    def equals(self, other): # reliably restored by inspect
        """
        Returns True if categorical arrays are equal.
        
                Parameters
                ----------
                other : `Categorical`
        
                Returns
                -------
                are_equal : boolean
        """
        pass

    def fillna(*args, **kwargs): # reliably restored by inspect
        """
        Fill NA/NaN values using the specified method.
        
                Parameters
                ----------
                method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
                    Method to use for filling holes in reindexed Series
                    pad / ffill: propagate last valid observation forward to next valid
                    backfill / bfill: use NEXT valid observation to fill gap
                value : scalar
                    Value to use to fill holes (e.g. 0)
                limit : int, default None
                    (Not implemented yet for Categorical!)
                    If method is specified, this is the maximum number of consecutive
                    NaN values to forward/backward fill. In other words, if there is
                    a gap with more than this number of consecutive NaNs, it will only
                    be partially filled. If method is not specified, this is the
                    maximum number of entries along the entire axis where NaNs will be
                    filled.
        
                Returns
                -------
                filled : Categorical with NA/NaN filled
        """
        pass

    @classmethod
    def from_array(cls, *args, **kwargs): # real signature unknown
        """
        .. deprecated:: 0.19.0
                   Use ``Categorical`` instead.
        
                Make a Categorical type from a single array-like object.
        
                For internal compatibility with numpy arrays.
        
                Parameters
                ----------
                data : array-like
                    Can be an Index or array-like. The categories are assumed to be
                    the unique values of `data`.
        """
        pass

    @classmethod
    def from_codes(cls, *args, **kwargs): # real signature unknown
        """
        Make a Categorical type from codes and categories arrays.
        
                This constructor is useful if you already have codes and categories and
                so do not need the (computation intensive) factorization step, which is
                usually done on the constructor.
        
                If your data does not follow this convention, please use the normal
                constructor.
        
                Parameters
                ----------
                codes : array-like, integers
                    An integer array, where each integer points to a category in
                    categories or -1 for NaN
                categories : index-like
                    The categories for the categorical. Items need to be unique.
                ordered : boolean, (default False)
                    Whether or not this categorical is treated as a ordered
                    categorical. If not given, the resulting categorical will be
                    unordered.
        """
        pass

    def get_values(self): # reliably restored by inspect
        """
        Return the values.
        
                For internal compatibility with pandas formatting.
        
                Returns
                -------
                values : numpy array
                    A numpy array of the same dtype as categorical.categories.dtype or
                    Index if datetime / periods
        """
        pass

    def isna(self): # reliably restored by inspect
        """
        Detect missing values
        
                Both missing values (-1 in .codes) and NA as a category are detected.
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See also
                --------
                isna : top-level isna
                isnull : alias of isna
                Categorical.notna : boolean inverse of Categorical.isna
        """
        pass

    def isnull(self): # reliably restored by inspect
        """
        Detect missing values
        
                Both missing values (-1 in .codes) and NA as a category are detected.
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See also
                --------
                isna : top-level isna
                isnull : alias of isna
                Categorical.notna : boolean inverse of Categorical.isna
        """
        pass

    def is_dtype_equal(self, other): # reliably restored by inspect
        """
        Returns True if categoricals are the same dtype
                  same categories, and same ordered
        
                Parameters
                ----------
                other : Categorical
        
                Returns
                -------
                are_equal : boolean
        """
        pass

    def map(self, mapper): # reliably restored by inspect
        """
        Apply mapper function to its categories (not codes).
        
                Parameters
                ----------
                mapper : callable
                    Function to be applied. When all categories are mapped
                    to different categories, the result will be Categorical which has
                    the same order property as the original. Otherwise, the result will
                    be np.ndarray.
        
                Returns
                -------
                applied : Categorical or Index.
        """
        pass

    def max(self, numeric_only=None, **kwargs): # reliably restored by inspect
        """
        The maximum value of the object.
        
                Only ordered `Categoricals` have a maximum!
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                max : the maximum of this `Categorical`
        """
        pass

    def memory_usage(self, deep=False): # reliably restored by inspect
        """
        Memory usage of my values
        
                Parameters
                ----------
                deep : bool
                    Introspect the data deeply, interrogate
                    `object` dtypes for system-level memory consumption
        
                Returns
                -------
                bytes used
        
                Notes
                -----
                Memory usage does not include memory consumed by elements that
                are not components of the array if deep=False
        
                See Also
                --------
                numpy.ndarray.nbytes
        """
        pass

    def min(self, numeric_only=None, **kwargs): # reliably restored by inspect
        """
        The minimum value of the object.
        
                Only ordered `Categoricals` have a minimum!
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                min : the minimum of this `Categorical`
        """
        pass

    def mode(self): # reliably restored by inspect
        """
        Returns the mode(s) of the Categorical.
        
                Always returns `Categorical` even if only one value.
        
                Returns
                -------
                modes : `Categorical` (sorted)
        """
        pass

    def notna(self): # reliably restored by inspect
        """
        Inverse of isna
        
                Both missing values (-1 in .codes) and NA as a category are detected as
                null.
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See also
                --------
                notna : top-level notna
                notnull : alias of notna
                Categorical.isna : boolean inverse of Categorical.notna
        """
        pass

    def notnull(self): # reliably restored by inspect
        """
        Inverse of isna
        
                Both missing values (-1 in .codes) and NA as a category are detected as
                null.
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See also
                --------
                notna : top-level notna
                notnull : alias of notna
                Categorical.isna : boolean inverse of Categorical.notna
        """
        pass

    def put(self, *args, **kwargs): # reliably restored by inspect
        """ Replace specific elements in the Categorical with given values. """
        pass

    def ravel(self, order=None): # reliably restored by inspect
        """
        Return a flattened (numpy) array.
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                raveled : numpy array
        """
        pass

    def remove_categories(self, removals, inplace=False): # reliably restored by inspect
        """
        Removes the specified categories.
        
                `removals` must be included in the old categories. Values which were in
                the removed categories will be set to NaN
        
                Raises
                ------
                ValueError
                    If the removals are not contained in the categories
        
                Parameters
                ----------
                removals : category or list of categories
                   The categories which should be removed.
                inplace : boolean (default: False)
                   Whether or not to remove the categories inplace or return a copy of
                   this categorical with removed categories.
        
                Returns
                -------
                cat : Categorical with removed categories or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_unused_categories
                set_categories
        """
        pass

    def remove_unused_categories(self, inplace=False): # reliably restored by inspect
        """
        Removes categories which are not used.
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to drop unused categories inplace or return a copy of
                   this categorical with unused categories dropped.
        
                Returns
                -------
                cat : Categorical with unused categories dropped or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                set_categories
        """
        pass

    def rename_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Renames categories.
        
                Raises
                ------
                ValueError
                    If new categories are list-like and do not have the same number of
                    items than the current categories or do not validate as categories
        
                Parameters
                ----------
                new_categories : list-like or dict-like
        
                   * list-like: all items must be unique and the number of items in
                     the new categories must match the existing number of categories.
        
                   * dict-like: specifies a mapping from
                     old categories to new. Categories not contained in the mapping
                     are passed through and extra categories in the mapping are
                     ignored. *New in version 0.21.0*.
        
                   .. warning::
        
                      Currently, Series are considered list like. In a future version
                      of pandas they'll be considered dict-like.
        
                inplace : boolean (default: False)
                   Whether or not to rename the categories inplace or return a copy of
                   this categorical with renamed categories.
        
                Returns
                -------
                cat : Categorical or None
                   With ``inplace=False``, the new categorical is returned.
                   With ``inplace=True``, there is no return value.
        
                See also
                --------
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        
                Examples
                --------
                >>> c = Categorical(['a', 'a', 'b'])
                >>> c.rename_categories([0, 1])
                [0, 0, 1]
                Categories (2, int64): [0, 1]
        
                For dict-like ``new_categories``, extra keys are ignored and
                categories not in the dictionary are passed through
        
                >>> c.rename_categories({'a': 'A', 'c': 'C'})
                [A, A, b]
                Categories (2, object): [A, b]
        """
        pass

    def reorder_categories(self, new_categories, ordered=None, inplace=False): # reliably restored by inspect
        """
        Reorders categories as specified in new_categories.
        
                `new_categories` need to include all old categories and no new category
                items.
        
                Raises
                ------
                ValueError
                    If the new categories do not contain all old category items or any
                    new ones
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : boolean, optional
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                inplace : boolean (default: False)
                   Whether or not to reorder the categories inplace or return a copy of
                   this categorical with reordered categories.
        
                Returns
                -------
                cat : Categorical with reordered categories or None if inplace.
        
                See also
                --------
                rename_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def repeat(self, repeats, *args, **kwargs): # reliably restored by inspect
        """
        Repeat elements of a Categorical.
        
                See also
                --------
                numpy.ndarray.repeat
        """
        pass

    def reshape(self, new_shape, *args, **kwargs): # reliably restored by inspect
        """
        .. deprecated:: 0.19.0
                   Calling this method will raise an error in a future release.
        
                An ndarray-compatible method that returns `self` because
                `Categorical` instances cannot actually be reshaped.
        
                Parameters
                ----------
                new_shape : int or tuple of ints
                    A 1-D array of integers that correspond to the new
                    shape of the `Categorical`. For more information on
                    the parameter, please refer to `np.reshape`.
        """
        pass

    def searchsorted(*args, **kwargs): # reliably restored by inspect
        """
        Find indices where elements should be inserted to maintain order.
        
                Find the indices into a sorted Categorical `self` such that, if the
                corresponding elements in `value` were inserted before the indices,
                the order of `self` would be preserved.
        
                Parameters
                ----------
                value : array_like
                    Values to insert into `self`.
                side : {'left', 'right'}, optional
                    If 'left', the index of the first suitable location found is given.
                    If 'right', return the last such index.  If there is no suitable
                    index, return either 0 or N (where N is the length of `self`).
                sorter : 1-D array_like, optional
                    Optional array of integer indices that sort `self` into ascending
                    order. They are typically the result of ``np.argsort``.
        
                Returns
                -------
                indices : array of ints
                    Array of insertion points with the same shape as `value`.
        
                See Also
                --------
                numpy.searchsorted
        
                Notes
                -----
                Binary search is used to find the required insertion points.
        
                Examples
                --------
        
                >>> x = pd.Series([1, 2, 3])
                >>> x
                0    1
                1    2
                2    3
                dtype: int64
        
                >>> x.searchsorted(4)
                array([3])
        
                >>> x.searchsorted([0, 4])
                array([0, 3])
        
                >>> x.searchsorted([1, 3], side='left')
                array([0, 2])
        
                >>> x.searchsorted([1, 3], side='right')
                array([1, 3])
        
                >>> x = pd.Categorical(['apple', 'bread', 'bread', 'cheese', 'milk' ])
                [apple, bread, bread, cheese, milk]
                Categories (4, object): [apple < bread < cheese < milk]
        
                >>> x.searchsorted('bread')
                array([1])     # Note: an array, not a scalar
        
                >>> x.searchsorted(['bread'])
                array([1])
        
                >>> x.searchsorted(['bread', 'eggs'])
                array([1, 4])
        
                >>> x.searchsorted(['bread', 'eggs'], side='right')
                array([3, 4])    # eggs before milk
        """
        pass

    def set_categories(self, new_categories, ordered=None, rename=False, inplace=False): # reliably restored by inspect
        """
        Sets the categories to the specified new_categories.
        
                `new_categories` can include new categories (which will result in
                unused categories) or remove old categories (which results in values
                set to NaN). If `rename==True`, the categories will simple be renamed
                (less or more items than in old categories will result in values set to
                NaN or in unused categories respectively).
        
                This method can be used to perform more than one action of adding,
                removing, and reordering simultaneously and is therefore faster than
                performing the individual steps via the more specialised methods.
        
                On the other hand this methods does not do checks (e.g., whether the
                old categories are included in the new categories on a reorder), which
                can result in surprising changes, for example when using special string
                dtypes on python3, which does not considers a S1 string equal to a
                single char python string.
        
                Raises
                ------
                ValueError
                    If new_categories does not validate as categories
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : boolean, (default: False)
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                rename : boolean (default: False)
                   Whether or not the new_categories should be considered as a rename
                   of the old  categories or as reordered categories.
                inplace : boolean (default: False)
                   Whether or not to reorder the categories inplace or return a copy of
                   this categorical with reordered categories.
        
                Returns
                -------
                cat : Categorical with reordered categories or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
        """
        pass

    def set_ordered(self, value, inplace=False): # reliably restored by inspect
        """
        Sets the ordered attribute to the boolean value
        
                Parameters
                ----------
                value : boolean to set whether this categorical is ordered (True) or
                   not (False)
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to the value
        """
        pass

    def shift(self, periods): # reliably restored by inspect
        """
        Shift Categorical by desired number of periods.
        
                Parameters
                ----------
                periods : int
                    Number of periods to move, can be positive or negative
        
                Returns
                -------
                shifted : Categorical
        """
        pass

    def sort_values(self, inplace=False, ascending=True, na_position=None): # reliably restored by inspect
        """
        Sorts the Categorical by category value returning a new
                Categorical by default.
        
                While an ordering is applied to the category values, sorting in this
                context refers more to organizing and grouping together based on
                matching category values. Thus, this function can be called on an
                unordered Categorical instance unlike the functions 'Categorical.min'
                and 'Categorical.max'.
        
                Parameters
                ----------
                inplace : boolean, default False
                    Do operation in place.
                ascending : boolean, default True
                    Order ascending. Passing False orders descending. The
                    ordering parameter provides the method by which the
                    category values are organized.
                na_position : {'first', 'last'} (optional, default='last')
                    'first' puts NaNs at the beginning
                    'last' puts NaNs at the end
        
                Returns
                -------
                y : Categorical or None
        
                See Also
                --------
                Categorical.sort
                Series.sort_values
        
                Examples
                --------
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
                >>> c
                [1, 2, 2, 1, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values()
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values(ascending=False)
                [5, 2, 2, 1, 1]
                Categories (3, int64): [1, 2, 5]
        
                Inplace sorting can be done as well:
        
                >>> c.sort_values(inplace=True)
                >>> c
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>>
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
        
                'sort_values' behaviour with NaNs. Note that 'na_position'
                is independent of the 'ascending' parameter:
        
                >>> c = pd.Categorical([np.nan, 2, 2, np.nan, 5])
                >>> c
                [NaN, 2.0, 2.0, NaN, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values()
                [2.0, 2.0, 5.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False)
                [5.0, 2.0, 2.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(na_position='first')
                [NaN, NaN, 2.0, 2.0, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False, na_position='first')
                [NaN, NaN, 5.0, 2.0, 2.0]
                Categories (2, int64): [2, 5]
        """
        pass

    def take(self, indexer, allow_fill=True, fill_value=None): # reliably restored by inspect
        """
        Take the codes by the indexer, fill with the fill_value.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def take_nd(self, indexer, allow_fill=True, fill_value=None): # reliably restored by inspect
        """
        Take the codes by the indexer, fill with the fill_value.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def tolist(self): # reliably restored by inspect
        """
        Return a list of the values.
        
                These are each a scalar type, which is a Python scalar
                (for str, int, float) or a pandas scalar
                (for Timestamp/Timedelta/Interval/Period)
        """
        pass

    def to_dense(self): # reliably restored by inspect
        """
        Return my 'dense' representation
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                dense : array
        """
        pass

    def unique(self): # reliably restored by inspect
        """
        Return the ``Categorical`` which ``categories`` and ``codes`` are
                unique. Unused categories are NOT returned.
        
                - unordered category: values and categories are sorted by appearance
                  order.
                - ordered category: values are sorted by appearance order, categories
                  keeps existing order.
        
                Returns
                -------
                unique values : ``Categorical``
        
                Examples
                --------
                An unordered Categorical will return categories in the
                order of appearance.
        
                >>> pd.Categorical(list('baabc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                >>> pd.Categorical(list('baabc'), categories=list('abc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                An ordered Categorical preserves the category ordering.
        
                >>> pd.Categorical(list('baabc'),
                ...                categories=list('abc'),
                ...                ordered=True)
                [b, a, c]
                Categories (3, object): [a < b < c]
        
                See Also
                --------
                unique
                CategoricalIndex.unique
                Series.unique
        """
        pass

    def value_counts(self, dropna=True): # reliably restored by inspect
        """
        Returns a Series containing counts of each category.
        
                Every category will have an entry, even those with a count of 0.
        
                Parameters
                ----------
                dropna : boolean, default True
                    Don't include counts of NaN, even if NaN is a category.
        
                Returns
                -------
                counts : Series
        
                See Also
                --------
                Series.value_counts
        """
        pass

    def view(self): # reliably restored by inspect
        """
        Return a view of myself.
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                view : Categorical
                   Returns `self`!
        """
        pass

    def _codes_for_groupby(self, sort): # reliably restored by inspect
        """
        If sort=False, return a copy of self, coded with categories as
                returned by .unique(), followed by any categories not appearing in
                the data. If sort=True, return self.
        
                This method is needed solely to ensure the categorical index of the
                GroupBy result has categories in the order of appearance in the data
                (GH-8868).
        
                Parameters
                ----------
                sort : boolean
                    The value of the sort paramter groupby was called with.
        
                Returns
                -------
                Categorical
                    If sort=False, the new categories are set to the order of
                    appearance in codes (unless ordered=True, in which case the
                    original order is preserved), followed by any unrepresented
                    categories in the original order.
        """
        pass

    @classmethod
    def _from_inferred_categories(cls, *args, **kwargs): # real signature unknown
        """
        Construct a Categorical from inferred values
        
                For inferred categories (`dtype` is None) the categories are sorted.
                For explicit `dtype`, the `inferred_categories` are cast to the
                appropriate type.
        
                Parameters
                ----------
        
                inferred_categories : Index
                inferred_codes : Index
                dtype : CategoricalDtype or 'category'
        
                Returns
                -------
                Categorical
        """
        pass

    def _get_codes(self): # reliably restored by inspect
        """
        Get the codes.
        
                Returns
                -------
                codes : integer array view
                    A non writable view of the `codes` array.
        """
        pass

    def _get_labels(self): # reliably restored by inspect
        """
        Get the category labels (deprecated).
        
                Deprecated, use .codes!
        """
        pass

    def _get_repr(self, length=True, na_rep=None, footer=True): # reliably restored by inspect
        # no doc
        pass

    def _maybe_coerce_indexer(self, indexer): # reliably restored by inspect
        """ return an indexer coerced to the codes dtype """
        pass

    def _reduce(self, op, name, axis=0, skipna=True, numeric_only=None, filter_type=None, **kwds): # reliably restored by inspect
        """ perform the reduction type operation """
        pass

    def _repr_categories(self): # reliably restored by inspect
        """ return the base repr for the categories """
        pass

    def _repr_categories_info(self): # reliably restored by inspect
        """ Returns a string representation of the footer. """
        pass

    def _repr_footer(self): # reliably restored by inspect
        # no doc
        pass

    def _reverse_indexer(self): # reliably restored by inspect
        """
        Compute the inverse of a categorical, returning
                a dict of categories -> indexers.
        
                *This is an internal function*
        
                Returns
                -------
                dict of categories -> indexers
        
                Example
                -------
                In [1]: c = pd.Categorical(list('aabca'))
        
                In [2]: c
                Out[2]:
                [a, a, b, c, a]
                Categories (3, object): [a, b, c]
        
                In [3]: c.categories
                Out[3]: Index([u'a', u'b', u'c'], dtype='object')
        
                In [4]: c.codes
                Out[4]: array([0, 0, 1, 2, 0], dtype=int8)
        
                In [5]: c._reverse_indexer()
                Out[5]: {'a': array([0, 1, 4]), 'b': array([2]), 'c': array([3])}
        """
        pass

    def _set_categories(self, categories, fastpath=False): # reliably restored by inspect
        """
        Sets new categories inplace
        
                Parameters
                ----------
                fastpath : boolean (default: False)
                   Don't perform validation of the categories for uniqueness or nulls
        
                Examples
                --------
                >>> c = Categorical(['a', 'b'])
                >>> c
                [a, b]
                Categories (2, object): [a, b]
        
                >>> c._set_categories(pd.Index(['a', 'c']))
                >>> c
                [a, c]
                Categories (2, object): [a, c]
        """
        pass

    def _set_codes(self, codes): # reliably restored by inspect
        """ Not settable by the user directly """
        pass

    def _set_dtype(self, dtype): # reliably restored by inspect
        """
        Internal method for directly updating the CategoricalDtype
        
                Parameters
                ----------
                dtype : CategoricalDtype
        
                Notes
                -----
                We don't do any validation here. It's assumed that the dtype is
                a (valid) instance of `CategoricalDtype`.
        """
        pass

    def _slice(self, slicer): # reliably restored by inspect
        """
        Return a slice of myself.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def _tidy_repr(self, max_vals=10, footer=True): # reliably restored by inspect
        """
        a short repr displaying only max_vals and an optional (but default
                footer)
        """
        pass

    def _values_for_rank(self): # reliably restored by inspect
        """
        For correctly ranking ordered categorical data. See GH#15420
        
                Ordered categorical data should be ranked on the basis of
                codes with -1 translated to NaN.
        
                Returns
                -------
                numpy array
        """
        pass

    def __array__(self, dtype=None): # reliably restored by inspect
        """
        The numpy array interface.
        
                Returns
                -------
                values : numpy array
                    A numpy array of either the specified dtype or,
                    if dtype==None (default), the same dtype as
                    categorical.categories.dtype
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        """ Return an item. """
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, values, categories=None, ordered=None, dtype=None, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Returns an Iterator over the values of this Categorical. """
        pass

    def __len__(self): # reliably restored by inspect
        """ The length of this Categorical. """
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        """
        Item assignment.
        
        
                Raises
                ------
                ValueError
                    If (one or more) Value is not in categories or if a assigned
                    `Categorical` does not have the same categories
        """
        pass

    def __setstate__(self, state): # reliably restored by inspect
        """ Necessary for making this object picklable """
        pass

    def __unicode__(self): # reliably restored by inspect
        """ Unicode representation. """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ compat, we are always our own object """

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The categories of this categorical.

        Setting assigns new values to each category (effectively a rename of
        each individual category).

        The assigned value has to be a list-like object. All items must be
        unique and the number of items in the new categories must be the same
        as the number of items in the old categories.

        Assigning to `categories` is a inplace operation!

        Raises
        ------
        ValueError
            If the new categories do not validate as categories or if the
            number of new categories is unequal the number of old categories

        See also
        --------
        rename_categories
        reorder_categories
        add_categories
        remove_categories
        remove_unused_categories
        set_categories
        """

    codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category codes of this categorical.

Level codes are an array if integer which are the positions of the real
values in the categories array.

There is not setter, use the other categorical methods and the normal item
setter to change values in the categorical.
"""

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :ref:`~pandas.api.types.CategoricalDtype` for this instance"""

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the category labels (deprecated).

        Deprecated, use .codes!
        """

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the categories have an ordered relationship"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Shape of the Categorical.

        For internal compatibility with numpy arrays.

        Returns
        -------
        shape : tuple
        """

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    itemsize = None
    ndim = None
    size = None
    _codes = None
    _deprecations = None # (!) real value is ''
    _dtype = None # (!) real value is ''
    _typ = 'categorical'
    __array_priority__ = 1000
    __hash__ = None


class CategoricalDtype(__pandas_core_dtypes_dtypes.ExtensionDtype):
    """
    Type for categorical data with the categories and orderedness
    
        .. versionchanged:: 0.21.0
    
        Parameters
        ----------
        categories : sequence, optional
            Must be unique, and must not contain any nulls.
        ordered : bool, default False
    
        Notes
        -----
        This class is useful for specifying the type of a ``Categorical``
        independent of the values. See :ref:`categorical.categoricaldtype`
        for more.
    
        Examples
        --------
        >>> t = CategoricalDtype(categories=['b', 'a'], ordered=True)
        >>> pd.Series(['a', 'b', 'a', 'c'], dtype=t)
        0      a
        1      b
        2      a
        3    NaN
        dtype: category
        Categories (2, object): [b < a]
    
        See Also
        --------
        pandas.Categorical
    """
    @classmethod
    def construct_from_string(cls, *args, **kwargs): # real signature unknown
        """
        attempt to construct this type from a string, raise a TypeError if
                it's not possible
        """
        pass

    def _finalize(self, categories, ordered, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _from_categorical_dtype(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_fastpath(cls, *args, **kwargs): # real signature unknown
        pass

    def _hash_categories(categories, ordered=True): # reliably restored by inspect
        # no doc
        pass

    def _validate_categories(categories, fastpath=False): # reliably restored by inspect
        """
        Validates that we have good categories
        
                Parameters
                ----------
                categories : array-like
                fastpath : bool
                    Whether to skip nan and uniqueness checks
        
                Returns
                -------
                categories : Index
        """
        pass

    def _validate_ordered(ordered): # reliably restored by inspect
        """
        Validates that we have a valid ordered parameter. If
                it is not a boolean, a TypeError will be raised.
        
                Parameters
                ----------
                ordered : object
                    The parameter to be verified.
        
                Raises
                ------
                TypeError
                    If 'ordered' is not a boolean.
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, categories=None, ordered=False): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        An ``Index`` containing the unique categories allowed.
        """

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the categories have an ordered relationship"""


    base = None # (!) real value is ''
    kind = 'O'
    name = 'category'
    str = '|O08'
    type = None # (!) real value is ''
    _cache = {}
    _metadata = [
        'categories',
        'ordered',
    ]


class ParserError(ValueError):
    """ Exception that is raised by an error encountered in `pd.read_csv`. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



CParserError = ParserError


class DtypeWarning(Warning):
    """
    Warning that is raised for a dtype incompatiblity. This
        can happen whenever `pd.read_csv` encounters non-
        uniform dtypes in a column(s) of a given CSV file.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class EmptyDataError(ValueError):
    """
    Exception that is thrown in `pd.read_csv` (by both the C and
        Python engines) when empty data or header is encountered.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class k(__numpy.generic):
    """ Any Python object.  Character code: 'O'. """
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ParserWarning(Warning):
    """
    Warning that is raised in `pd.read_csv` whenever it is necessary
        to change parsers (generally from 'c' to 'python') contrary to the
        one specified by the user due to lack of support or functionality for
        parsing particular attributes of a CSV file with the requsted engine.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TextReader(object):
    """ # source: StringIO or file object """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def debug_print(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_bad_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def _set_quoting(self, *args, **kwargs): # real signature unknown
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

    allow_leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_recarray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compact_ints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delim_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype_cast_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    low_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mangle_dupe_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    memory_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    noconvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipfooter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tupleize_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_unsigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

na_values = {
    np.double: 
        nan
    ,
    np.intp: 
        -9223372036854775808
    ,
    np.int32: 
        -2147483648
    ,
    np.short: 
        -32768
    ,
    np.byte: 
        -128
    ,
    np.uint: 
        18446744073709551615
    ,
    np.uint32: 
        4294967295
    ,
    np.ushort: 
        65535
    ,
    np.ubyte: 
        255
    ,
    np.bool8: 
        255
    ,
    np.object0: 
        nan
    ,
    None:  # (!) real value is ''
        nan
    ,
    None:  # (!) real value is ''
        -9223372036854775808
    ,
    None:  # (!) real value is ''
        -2147483648
    ,
    None:  # (!) real value is ''
        -32768
    ,
    None:  # (!) real value is ''
        -128
    ,
    None:  # (!) real value is ''
        18446744073709551615
    ,
    None:  # (!) real value is ''
        4294967295
    ,
    None:  # (!) real value is ''
        65535
    ,
    None:  # (!) real value is ''
        255
    ,
    None:  # (!) real value is ''
        255
    ,
    None:  # (!) real value is ''
        nan
    ,
}

_NA_VALUES = [
    b'1.#IND',
    b'#N/A N/A',
    b'#NA',
    b'',
    b'#N/A',
    b'null',
    b'nan',
    b'NA',
    b'n/a',
    b'NULL',
    b'-nan',
    b'N/A',
    b'-1.#IND',
    b'-NaN',
    b'-1.#QNAN',
    b'NaN',
    b'1.#QNAN',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}


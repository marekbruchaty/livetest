# encoding: utf-8
# module pandas._libs.testing
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/testing.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import pandas.compat as compat # /usr/local/lib/python3.6/site-packages/pandas/compat/__init__.py

# functions

def array_equivalent(left, right, strict_nan=False): # reliably restored by inspect
    """
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
        in corresponding locations.  False otherwise. It is assumed that left and
        right are NumPy arrays of the same dtype. The behavior of this function
        (particularly with respect to NaNs) is not defined if the dtypes are
        different.
    
        Parameters
        ----------
        left, right : ndarrays
        strict_nan : bool, default False
            If True, consider NaN and None to be different.
    
        Returns
        -------
        b : bool
            Returns True if the arrays are equivalent.
    
        Examples
        --------
        >>> array_equivalent(
        ...     np.array([1, 2, np.nan]),
        ...     np.array([1, 2, np.nan]))
        True
        >>> array_equivalent(
        ...     np.array([1, np.nan, 2]),
        ...     np.array([1, 2, np.nan]))
        False
    """
    pass

def assert_almost_equal(*args, **kwargs): # real signature unknown
    """
    Check that left and right objects are almost equal.
    
        Parameters
        ----------
        a : object
        b : object
        check_less_precise : bool or int, default False
            Specify comparison precision.
            5 digits (False) or 3 digits (True) after decimal points are
            compared. If an integer, then this will be the number of decimal
            points to compare
        check_dtype: bool, default True
            check dtype if both a and b are np.ndarray
        obj : str, default None
            Specify object name being compared, internally used to show
            appropriate assertion message
        lobj : str, default None
            Specify left object name being compared, internally used to show
            appropriate assertion message
        robj : str, default None
            Specify right object name being compared, internally used to show
            appropriate assertion message
    """
    pass

def assert_dict_equal(*args, **kwargs): # real signature unknown
    pass

def isna(obj): # reliably restored by inspect
    """
    Detect missing values (NaN in numeric arrays, None/NaN in object arrays)
    
        Parameters
        ----------
        arr : ndarray or object value
            Object to check for null-ness
    
        Returns
        -------
        isna : array-like of bool or bool
            Array or bool indicating whether an object is null or if an array is
            given which of the element is null.
    
        See also
        --------
        pandas.notna: boolean inverse of pandas.isna
        pandas.isnull: alias of isna
    """
    pass

def is_dtype_equal(source, target): # reliably restored by inspect
    """
    Check if two dtypes are equal.
    
        Parameters
        ----------
        source : The first dtype to compare
        target : The second dtype to compare
    
        Returns
        ----------
        boolean : Whether or not the two dtypes are equal.
    
        Examples
        --------
        >>> is_dtype_equal(int, float)
        False
        >>> is_dtype_equal("int", int)
        True
        >>> is_dtype_equal(object, "category")
        False
        >>> is_dtype_equal(CategoricalDtype(), "category")
        True
        >>> is_dtype_equal(DatetimeTZDtype(), "datetime64")
        False
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}


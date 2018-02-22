# encoding: utf-8
# module pandas._libs.algos
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/algos.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import pandas._libs.lib as lib # /usr/local/lib/python3.6/site-packages/pandas/_libs/lib.cpython-36m-darwin.so

# functions

def arrmap_bool(*args, **kwargs): # real signature unknown
    pass

def arrmap_float32(*args, **kwargs): # real signature unknown
    pass

def arrmap_float64(*args, **kwargs): # real signature unknown
    pass

def arrmap_int32(*args, **kwargs): # real signature unknown
    pass

def arrmap_int64(*args, **kwargs): # real signature unknown
    pass

def arrmap_object(*args, **kwargs): # real signature unknown
    pass

def arrmap_uint64(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_bool(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_float32(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_float64(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_int32(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_int64(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_object(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace_uint64(*args, **kwargs): # real signature unknown
    pass

def backfill_bool(*args, **kwargs): # real signature unknown
    pass

def backfill_float32(*args, **kwargs): # real signature unknown
    pass

def backfill_float64(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_bool(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_float32(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_float64(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_int32(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_int64(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_object(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace_uint64(*args, **kwargs): # real signature unknown
    pass

def backfill_int32(*args, **kwargs): # real signature unknown
    pass

def backfill_int64(*args, **kwargs): # real signature unknown
    pass

def backfill_object(*args, **kwargs): # real signature unknown
    pass

def backfill_uint64(*args, **kwargs): # real signature unknown
    pass

def diff_2d_float32(*args, **kwargs): # real signature unknown
    pass

def diff_2d_float64(*args, **kwargs): # real signature unknown
    pass

def diff_2d_int16(*args, **kwargs): # real signature unknown
    pass

def diff_2d_int32(*args, **kwargs): # real signature unknown
    pass

def diff_2d_int64(*args, **kwargs): # real signature unknown
    pass

def diff_2d_int8(*args, **kwargs): # real signature unknown
    pass

def ensure_float32(*args, **kwargs): # real signature unknown
    pass

def ensure_float64(*args, **kwargs): # real signature unknown
    pass

def ensure_int16(*args, **kwargs): # real signature unknown
    pass

def ensure_int32(*args, **kwargs): # real signature unknown
    pass

def ensure_int64(*args, **kwargs): # real signature unknown
    pass

def ensure_int8(*args, **kwargs): # real signature unknown
    pass

def ensure_object(*args, **kwargs): # real signature unknown
    pass

def ensure_platform_int(*args, **kwargs): # real signature unknown
    pass

def ensure_uint64(*args, **kwargs): # real signature unknown
    pass

def groupsort_indexer(*args, **kwargs): # real signature unknown
    """
    compute a 1-d indexer that is an ordering of the passed index,
        ordered by the groups. This is a reverse of the label
        factorization process.
    
        Parameters
        ----------
        index: int64 ndarray
            mappings from group -> position
        ngroups: int64
            number of groups
    
        return a tuple of (1-d indexer ordered by groups, group counts)
    """
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_monotonic_bool(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_float32(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_float64(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_int32(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_int64(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_object(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def is_monotonic_uint64(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        is_monotonic_inc, is_monotonic_dec, is_unique
    """
    pass

def kth_smallest(*args, **kwargs): # real signature unknown
    pass

def map_indices_bool(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_float32(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_float64(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_int32(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_int64(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_object(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_indices_uint64(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def max_subseq(*args, **kwargs): # real signature unknown
    pass

def median(*args, **kwargs): # real signature unknown
    """ A faster median """
    pass

def min_subseq(*args, **kwargs): # real signature unknown
    pass

def nancorr(*args, **kwargs): # real signature unknown
    pass

def nancorr_spearman(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_bool(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_float32(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_float64(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_int32(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_int64(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_object(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace_uint64(*args, **kwargs): # real signature unknown
    pass

def pad_bool(*args, **kwargs): # real signature unknown
    pass

def pad_float32(*args, **kwargs): # real signature unknown
    pass

def pad_float64(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_bool(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_float32(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_float64(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_int32(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_int64(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_object(*args, **kwargs): # real signature unknown
    pass

def pad_inplace_uint64(*args, **kwargs): # real signature unknown
    pass

def pad_int32(*args, **kwargs): # real signature unknown
    pass

def pad_int64(*args, **kwargs): # real signature unknown
    pass

def pad_object(*args, **kwargs): # real signature unknown
    pass

def pad_uint64(*args, **kwargs): # real signature unknown
    pass

def put2d_float32_float32(*args, **kwargs): # real signature unknown
    pass

def put2d_float64_float64(*args, **kwargs): # real signature unknown
    pass

def put2d_int16_float32(*args, **kwargs): # real signature unknown
    pass

def put2d_int32_float64(*args, **kwargs): # real signature unknown
    pass

def put2d_int64_float64(*args, **kwargs): # real signature unknown
    pass

def put2d_int8_float32(*args, **kwargs): # real signature unknown
    pass

def rank_1d_float64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_1d_int64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_1d_object(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_1d_uint64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_2d_float64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_2d_int64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_2d_object(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def rank_2d_uint64(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of scipy.stats.rankdata """
    pass

def take_1d_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_1d_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_1d_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_object_object(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Infinity(object):
    """ provide a positive Infinity comparision method for ranking """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __hash__ = None


class NegInfinity(object):
    """ provide a negative Infinity comparision method for ranking """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __hash__ = None


# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    '__pyx_fuse_0kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_1kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_2kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_3kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_4kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_5kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_6kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_7kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_8kth_smallest': None, # (!) real value is ''
    '__pyx_fuse_9kth_smallest': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}


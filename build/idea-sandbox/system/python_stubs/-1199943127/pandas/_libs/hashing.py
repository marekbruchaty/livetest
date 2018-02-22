# encoding: utf-8
# module pandas._libs.hashing
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/hashing.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py

# functions

def hash_object_array(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        arr : 1-d object ndarray of objects
        key : hash key, must be 16 byte len encoded
        encoding : encoding for key & arr, default to 'utf8'
    
        Returns
        -------
        1-d uint64 ndarray of hashes
    
        Notes
        -----
        allowed values must be strings, or nulls
        mixed array types will raise TypeError
    """
    pass

def siphash(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}


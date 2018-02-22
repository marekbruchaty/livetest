# encoding: utf-8
# module pandas._libs.interval
# from /usr/local/lib/python3.6/site-packages/pandas/_libs/interval.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /usr/local/lib/python3.6/site-packages/numpy/__init__.py
import numbers as numbers # /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/lib/python3.6/numbers.py
from pandas._libs.tslib import Timestamp


# functions

def intervals_to_interval_bounds(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        intervals: ndarray object array of Intervals / nulls
    
        Returns
        -------
        tuples (left: ndarray object array,
                right: ndarray object array,
                closed: str)
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalMixin(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalTree(*args, **kwargs): # real signature unknown
    pass

# classes

class Float32ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float32ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float32ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float32ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float64ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float64ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float64ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Float64ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int32ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int32ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int32ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int32ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64ClosedBothIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64ClosedLeftIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64ClosedNeitherIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64ClosedRightIntervalNode(object):
    """
    Non-terminal node for an IntervalTree
    
        Categorizes intervals by those that fall to the left, those that fall to
        the right, and those that overlap with the pivot.
    """
    def counts(self, *args, **kwargs): # real signature unknown
        """
        Inspect counts on this node
                useful for debugging purposes
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Recursively query this node and its sub-nodes for intervals that
                overlap with the query point.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    is_leaf_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leaf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class IntervalMixin(object):
    # no doc
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

    closed_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    closed_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Interval(IntervalMixin):
    """
    Immutable object implementing an Interval, a bounded slice-like interval.
    
        .. versionadded:: 0.20.0
    
        Parameters
        ----------
        left : value
            Left bound for interval.
        right : value
            Right bound for interval.
        closed : {'left', 'right', 'both', 'neither'}
            Whether the interval is closed on the left-side, right-side, both or
            neither. Defaults to 'right'.
    
        Examples
        --------
        >>> iv = pd.Interval(left=0, right=5)
        >>> iv
        Interval(0, 5, closed='right')
        >>> 2.5 in iv
        True
    
        >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01'),
        ...                         pd.Timestamp('2017-12-31'), closed='both')
        >>> pd.Timestamp('2017-01-01 00:00') in year_2017
        True
    
        See Also
        --------
        IntervalIndex : an Index of ``interval`` s that are all closed on the same
                        side.
        cut, qcut : convert arrays of continuous data into categoricals/series of
                    ``Interval``.
    """
    def _repr_base(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __init__(self, left=0, right=5): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IntervalTree(IntervalMixin):
    """
    A centered interval tree
    
        Based off the algorithm described on Wikipedia:
        http://en.wikipedia.org/wiki/Interval_tree
    
        we are emulating the IndexEngine interface
    """
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def get_loc_interval(self, *args, **kwargs): # real signature unknown
        """
        Lookup the intervals enclosed in the given interval bounds
        
                The given interval is presumed to have closed bounds.
        """
        pass

    def _get_partial_overlap(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals with the given side
                falling between the left and right bounds of an interval query
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                left, right : np.ndarray[ndim=1]
                    Left and right bounds for each interval. Assumed to contain no
                    NaNs.
                closed : {'left', 'right', 'both', 'neither'}, optional
                    Whether the intervals are closed on the left-side, right-side, both
                    or neither. Defaults to 'right'.
                leaf_size : int, optional
                    Parameter that controls when the tree switches from creating nodes
                    to brute-force search. Tune this parameter to optimize query
                    performance.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __pyx_fuse_0get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_0get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_0get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_1get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_1get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_1get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_2get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_2get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_2get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __pyx_fuse_3get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_3get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_3get_loc(self, *args, **kwargs): # real signature unknown
        """
        Return all positions corresponding to intervals that overlap with
                the given scalar key
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the left labels; this is used for binary search
        """

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the right labels
        """

    root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

NODE_CLASSES = {
    (
        'float32',
        'both',
    ): 
        Float32ClosedBothIntervalNode
    ,
    (
        'float32',
        'left',
    ): 
        Float32ClosedLeftIntervalNode
    ,
    (
        'float32',
        'neither',
    ): 
        Float32ClosedNeitherIntervalNode
    ,
    (
        'float32',
        'right',
    ): 
        Float32ClosedRightIntervalNode
    ,
    (
        'float64',
        'both',
    ): 
        Float64ClosedBothIntervalNode
    ,
    (
        'float64',
        'left',
    ): 
        Float64ClosedLeftIntervalNode
    ,
    (
        'float64',
        'neither',
    ): 
        Float64ClosedNeitherIntervalNode
    ,
    (
        'float64',
        'right',
    ): 
        Float64ClosedRightIntervalNode
    ,
    (
        'int32',
        'both',
    ): 
        Int32ClosedBothIntervalNode
    ,
    (
        'int32',
        'left',
    ): 
        Int32ClosedLeftIntervalNode
    ,
    (
        'int32',
        'neither',
    ): 
        Int32ClosedNeitherIntervalNode
    ,
    (
        'int32',
        'right',
    ): 
        Int32ClosedRightIntervalNode
    ,
    (
        'int64',
        'both',
    ): 
        Int64ClosedBothIntervalNode
    ,
    (
        'int64',
        'left',
    ): 
        Int64ClosedLeftIntervalNode
    ,
    (
        'int64',
        'neither',
    ): 
        Int64ClosedNeitherIntervalNode
    ,
    (
        'int64',
        'right',
    ): 
        Int64ClosedRightIntervalNode
    ,
}

_VALID_CLOSED = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}


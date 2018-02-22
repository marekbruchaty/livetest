# encoding: utf-8
# module sqlalchemy.cresultproxy
# from /usr/local/lib/python3.6/site-packages/sqlalchemy/cresultproxy.cpython-36m-darwin.so
# by generator 1.145
""" Module containing C versions of core ResultProxy classes. """
# no imports

# functions

def safe_rowproxy_reconstructor(*args, **kwargs): # real signature unknown
    """ reconstruct a RowProxy instance from its pickled form. """
    pass

# classes

class BaseRowProxy(object):
    """ BaseRowProxy is a abstract base class for RowProxy """
    def values(self, *args, **kwargs): # real signature unknown
        """ Return the values represented by this BaseRowProxy as a list. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Pickle support method. """
        pass

    _keymap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Key to (processor, index) dict"""

    _parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ResultMetaData"""

    _processors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of type processors"""

    _row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Original row tuple"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''


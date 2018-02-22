# encoding: utf-8
# module numpy.core.umath
# from /usr/local/lib/python3.6/site-packages/numpy/core/umath.cpython-36m-darwin.so
# by generator 1.145
# no doc
# no imports

# Variables with simple values
e = 2.718281828459045

ERR_CALL = 3
ERR_DEFAULT = 521
ERR_IGNORE = 0
ERR_LOG = 5
ERR_PRINT = 4
ERR_RAISE = 2
ERR_WARN = 1

euler_gamma = 0.5772156649015329

FLOATING_POINT_SUPPORT = 1

FPE_DIVIDEBYZERO = 1
FPE_INVALID = 8
FPE_OVERFLOW = 2
FPE_UNDERFLOW = 4

NAN = nan

NINF = -inf

NZERO = -0.0

pi = 3.141592653589793

PINF = inf

PZERO = 0.0

SHIFT_DIVIDEBYZERO = 0
SHIFT_INVALID = 9
SHIFT_OVERFLOW = 3
SHIFT_UNDERFLOW = 6

UFUNC_BUFSIZE_DEFAULT = 8192

UFUNC_PYVALS_NAME = 'UFUNC_PYVALS'

__version__ = b'0.4.0'

# functions

def absolute(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Calculate the absolute value element-wise.
    
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
    absolute : ndarray
        An ndarray containing the absolute value of
        each element in `x`.  For complex input, ``a + ib``, the
        absolute value is :math:`\sqrt{ a^2 + b^2 }`.
    
    Examples
    --------
    >>> x = np.array([-1.2, 1.2])
    >>> np.absolute(x)
    array([ 1.2,  1.2])
    >>> np.absolute(1.2 + 1j)
    1.5620499351813308
    
    Plot the function over ``[-10, 10]``:
    
    >>> import matplotlib.pyplot as plt
    
    >>> x = np.linspace(start=-10, stop=10, num=101)
    >>> plt.plot(x, np.absolute(x))
    >>> plt.show()
    
    Plot the function over the complex plane:
    
    >>> xx = x + 1j * x[:, np.newaxis]
    >>> plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
    >>> plt.show()
    """
    pass

def add(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Add arguments element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays to be added.  If ``x1.shape != x2.shape``, they must be
        broadcastable to a common shape (which may be the shape of one or
        the other).
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
    add : ndarray or scalar
        The sum of `x1` and `x2`, element-wise.  Returns a scalar if
        both  `x1` and `x2` are scalars.
    
    Notes
    -----
    Equivalent to `x1` + `x2` in terms of array broadcasting.
    
    Examples
    --------
    >>> np.add(1.0, 4.0)
    5.0
    >>> x1 = np.arange(9.0).reshape((3, 3))
    >>> x2 = np.arange(3.0)
    >>> np.add(x1, x2)
    array([[  0.,   2.,   4.],
           [  3.,   5.,   7.],
           [  6.,   8.,  10.]])
    """
    pass

def arccos(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Trigonometric inverse cosine, element-wise.
    
    The inverse of `cos` so that, if ``y = cos(x)``, then ``x = arccos(y)``.
    
    Parameters
    ----------
    x : array_like
        `x`-coordinate on the unit circle.
        For real arguments, the domain is [-1, 1].
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
    angle : ndarray
        The angle of the ray intersecting the unit circle at the given
        `x`-coordinate in radians [0, pi]. If `x` is a scalar then a
        scalar is returned, otherwise an array of the same shape as `x`
        is returned.
    
    See Also
    --------
    cos, arctan, arcsin, emath.arccos
    
    Notes
    -----
    `arccos` is a multivalued function: for each `x` there are infinitely
    many numbers `z` such that `cos(z) = x`. The convention is to return
    the angle `z` whose real part lies in `[0, pi]`.
    
    For real-valued input data types, `arccos` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arccos` is a complex analytic function that
    has branch cuts `[-inf, -1]` and `[1, inf]` and is continuous from
    above on the former and from below on the latter.
    
    The inverse `cos` is also known as `acos` or cos^-1.
    
    References
    ----------
    M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
    10th printing, 1964, pp. 79. http://www.math.sfu.ca/~cbm/aands/
    
    Examples
    --------
    We expect the arccos of 1 to be 0, and of -1 to be pi:
    
    >>> np.arccos([1, -1])
    array([ 0.        ,  3.14159265])
    
    Plot arccos:
    
    >>> import matplotlib.pyplot as plt
    >>> x = np.linspace(-1, 1, num=100)
    >>> plt.plot(x, np.arccos(x))
    >>> plt.axis('tight')
    >>> plt.show()
    """
    pass

def arccosh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Inverse hyperbolic cosine, element-wise.
    
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
    arccosh : ndarray
        Array of the same shape as `x`.
    
    See Also
    --------
    
    cosh, arcsinh, sinh, arctanh, tanh
    
    Notes
    -----
    `arccosh` is a multivalued function: for each `x` there are infinitely
    many numbers `z` such that `cosh(z) = x`. The convention is to return the
    `z` whose imaginary part lies in `[-pi, pi]` and the real part in
    ``[0, inf]``.
    
    For real-valued input data types, `arccosh` always returns real output.
    For each value that cannot be expressed as a real number or infinity, it
    yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arccosh` is a complex analytical function that
    has a branch cut `[-inf, 1]` and is continuous from above on it.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 86. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Inverse hyperbolic function",
           http://en.wikipedia.org/wiki/Arccosh
    
    Examples
    --------
    >>> np.arccosh([np.e, 10.0])
    array([ 1.65745445,  2.99322285])
    >>> np.arccosh(1)
    0.0
    """
    pass

def arcsin(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Inverse sine, element-wise.
    
    Parameters
    ----------
    x : array_like
        `y`-coordinate on the unit circle.
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
    angle : ndarray
        The inverse sine of each element in `x`, in radians and in the
        closed interval ``[-pi/2, pi/2]``.  If `x` is a scalar, a scalar
        is returned, otherwise an array.
    
    See Also
    --------
    sin, cos, arccos, tan, arctan, arctan2, emath.arcsin
    
    Notes
    -----
    `arcsin` is a multivalued function: for each `x` there are infinitely
    many numbers `z` such that :math:`sin(z) = x`.  The convention is to
    return the angle `z` whose real part lies in [-pi/2, pi/2].
    
    For real-valued input data types, *arcsin* always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arcsin` is a complex analytic function that
    has, by convention, the branch cuts [-inf, -1] and [1, inf]  and is
    continuous from above on the former and from below on the latter.
    
    The inverse sine is also known as `asin` or sin^{-1}.
    
    References
    ----------
    Abramowitz, M. and Stegun, I. A., *Handbook of Mathematical Functions*,
    10th printing, New York: Dover, 1964, pp. 79ff.
    http://www.math.sfu.ca/~cbm/aands/
    
    Examples
    --------
    >>> np.arcsin(1)     # pi/2
    1.5707963267948966
    >>> np.arcsin(-1)    # -pi/2
    -1.5707963267948966
    >>> np.arcsin(0)
    0.0
    """
    pass

def arcsinh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Inverse hyperbolic sine element-wise.
    
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
    out : ndarray
        Array of of the same shape as `x`.
    
    Notes
    -----
    `arcsinh` is a multivalued function: for each `x` there are infinitely
    many numbers `z` such that `sinh(z) = x`. The convention is to return the
    `z` whose imaginary part lies in `[-pi/2, pi/2]`.
    
    For real-valued input data types, `arcsinh` always returns real output.
    For each value that cannot be expressed as a real number or infinity, it
    returns ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arccos` is a complex analytical function that
    has branch cuts `[1j, infj]` and `[-1j, -infj]` and is continuous from
    the right on the former and from the left on the latter.
    
    The inverse hyperbolic sine is also known as `asinh` or ``sinh^-1``.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 86. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Inverse hyperbolic function",
           http://en.wikipedia.org/wiki/Arcsinh
    
    Examples
    --------
    >>> np.arcsinh(np.array([np.e, 10.0]))
    array([ 1.72538256,  2.99822295])
    """
    pass

def arctan(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Trigonometric inverse tangent, element-wise.
    
    The inverse of tan, so that if ``y = tan(x)`` then ``x = arctan(y)``.
    
    Parameters
    ----------
    x : array_like
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
    out : ndarray
        Out has the same shape as `x`.  Its real part is in
        ``[-pi/2, pi/2]`` (``arctan(+/-inf)`` returns ``+/-pi/2``).
        It is a scalar if `x` is a scalar.
    
    See Also
    --------
    arctan2 : The "four quadrant" arctan of the angle formed by (`x`, `y`)
        and the positive `x`-axis.
    angle : Argument of complex values.
    
    Notes
    -----
    `arctan` is a multi-valued function: for each `x` there are infinitely
    many numbers `z` such that tan(`z`) = `x`.  The convention is to return
    the angle `z` whose real part lies in [-pi/2, pi/2].
    
    For real-valued input data types, `arctan` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arctan` is a complex analytic function that
    has [`1j, infj`] and [`-1j, -infj`] as branch cuts, and is continuous
    from the left on the former and from the right on the latter.
    
    The inverse tangent is also known as `atan` or tan^{-1}.
    
    References
    ----------
    Abramowitz, M. and Stegun, I. A., *Handbook of Mathematical Functions*,
    10th printing, New York: Dover, 1964, pp. 79.
    http://www.math.sfu.ca/~cbm/aands/
    
    Examples
    --------
    We expect the arctan of 0 to be 0, and of 1 to be pi/4:
    
    >>> np.arctan([0, 1])
    array([ 0.        ,  0.78539816])
    
    >>> np.pi/4
    0.78539816339744828
    
    Plot arctan:
    
    >>> import matplotlib.pyplot as plt
    >>> x = np.linspace(-10, 10)
    >>> plt.plot(x, np.arctan(x))
    >>> plt.axis('tight')
    >>> plt.show()
    """
    pass

def arctan2(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.
    
    The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is
    the signed angle in radians between the ray ending at the origin and
    passing through the point (1,0), and the ray ending at the origin and
    passing through the point (`x2`, `x1`).  (Note the role reversal: the
    "`y`-coordinate" is the first function parameter, the "`x`-coordinate"
    is the second.)  By IEEE convention, this function is defined for
    `x2` = +/-0 and for either or both of `x1` and `x2` = +/-inf (see
    Notes for specific values).
    
    This function is not defined for complex-valued arguments; for the
    so-called argument of complex values, use `angle`.
    
    Parameters
    ----------
    x1 : array_like, real-valued
        `y`-coordinates.
    x2 : array_like, real-valued
        `x`-coordinates. `x2` must be broadcastable to match the shape of
        `x1` or vice versa.
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
    angle : ndarray
        Array of angles in radians, in the range ``[-pi, pi]``.
    
    See Also
    --------
    arctan, tan, angle
    
    Notes
    -----
    *arctan2* is identical to the `atan2` function of the underlying
    C library.  The following special values are defined in the C
    standard: [1]_
    
    ====== ====== ================
    `x1`   `x2`   `arctan2(x1,x2)`
    ====== ====== ================
    +/- 0  +0     +/- 0
    +/- 0  -0     +/- pi
     > 0   +/-inf +0 / +pi
     < 0   +/-inf -0 / -pi
    +/-inf +inf   +/- (pi/4)
    +/-inf -inf   +/- (3*pi/4)
    ====== ====== ================
    
    Note that +0 and -0 are distinct floating point numbers, as are +inf
    and -inf.
    
    References
    ----------
    .. [1] ISO/IEC standard 9899:1999, "Programming language C."
    
    Examples
    --------
    Consider four points in different quadrants:
    
    >>> x = np.array([-1, +1, +1, -1])
    >>> y = np.array([-1, -1, +1, +1])
    >>> np.arctan2(y, x) * 180 / np.pi
    array([-135.,  -45.,   45.,  135.])
    
    Note the order of the parameters. `arctan2` is defined also when `x2` = 0
    and at several other special points, obtaining values in
    the range ``[-pi, pi]``:
    
    >>> np.arctan2([1., -1.], [0., 0.])
    array([ 1.57079633, -1.57079633])
    >>> np.arctan2([0., 0., np.inf], [+0., -0., np.inf])
    array([ 0.        ,  3.14159265,  0.78539816])
    """
    pass

def arctanh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Inverse hyperbolic tangent element-wise.
    
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
    out : ndarray
        Array of the same shape as `x`.
    
    See Also
    --------
    emath.arctanh
    
    Notes
    -----
    `arctanh` is a multivalued function: for each `x` there are infinitely
    many numbers `z` such that `tanh(z) = x`. The convention is to return
    the `z` whose imaginary part lies in `[-pi/2, pi/2]`.
    
    For real-valued input data types, `arctanh` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `arctanh` is a complex analytical function
    that has branch cuts `[-1, -inf]` and `[1, inf]` and is continuous from
    above on the former and from below on the latter.
    
    The inverse hyperbolic tangent is also known as `atanh` or ``tanh^-1``.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 86. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Inverse hyperbolic function",
           http://en.wikipedia.org/wiki/Arctanh
    
    Examples
    --------
    >>> np.arctanh([0, -0.5])
    array([ 0.        , -0.54930614])
    """
    pass

def bitwise_and(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the bit-wise AND of two arrays element-wise.
    
    Computes the bit-wise AND of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``&``.
    
    Parameters
    ----------
    x1, x2 : array_like
        Only integer and boolean types are handled.
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
    out : array_like
        Result.
    
    See Also
    --------
    logical_and
    bitwise_or
    bitwise_xor
    binary_repr :
        Return the binary representation of the input number as a string.
    
    Examples
    --------
    The number 13 is represented by ``00001101``.  Likewise, 17 is
    represented by ``00010001``.  The bit-wise AND of 13 and 17 is
    therefore ``000000001``, or 1:
    
    >>> np.bitwise_and(13, 17)
    1
    
    >>> np.bitwise_and(14, 13)
    12
    >>> np.binary_repr(12)
    '1100'
    >>> np.bitwise_and([14,3], 13)
    array([12,  1])
    
    >>> np.bitwise_and([11,7], [4,25])
    array([0, 1])
    >>> np.bitwise_and(np.array([2,5,255]), np.array([3,14,16]))
    array([ 2,  4, 16])
    >>> np.bitwise_and([True, True], [False, True])
    array([False,  True], dtype=bool)
    """
    pass

def bitwise_or(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the bit-wise OR of two arrays element-wise.
    
    Computes the bit-wise OR of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``|``.
    
    Parameters
    ----------
    x1, x2 : array_like
        Only integer and boolean types are handled.
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
    out : array_like
        Result.
    
    See Also
    --------
    logical_or
    bitwise_and
    bitwise_xor
    binary_repr :
        Return the binary representation of the input number as a string.
    
    Examples
    --------
    The number 13 has the binaray representation ``00001101``. Likewise,
    16 is represented by ``00010000``.  The bit-wise OR of 13 and 16 is
    then ``000111011``, or 29:
    
    >>> np.bitwise_or(13, 16)
    29
    >>> np.binary_repr(29)
    '11101'
    
    >>> np.bitwise_or(32, 2)
    34
    >>> np.bitwise_or([33, 4], 1)
    array([33,  5])
    >>> np.bitwise_or([33, 4], [1, 2])
    array([33,  6])
    
    >>> np.bitwise_or(np.array([2, 5, 255]), np.array([4, 4, 4]))
    array([  6,   5, 255])
    >>> np.array([2, 5, 255]) | np.array([4, 4, 4])
    array([  6,   5, 255])
    >>> np.bitwise_or(np.array([2, 5, 255, 2147483647L], dtype=np.int32),
    ...               np.array([4, 4, 4, 2147483647L], dtype=np.int32))
    array([         6,          5,        255, 2147483647])
    >>> np.bitwise_or([True, True], [False, True])
    array([ True,  True], dtype=bool)
    """
    pass

def bitwise_xor(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the bit-wise XOR of two arrays element-wise.
    
    Computes the bit-wise XOR of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``^``.
    
    Parameters
    ----------
    x1, x2 : array_like
        Only integer and boolean types are handled.
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
    out : array_like
        Result.
    
    See Also
    --------
    logical_xor
    bitwise_and
    bitwise_or
    binary_repr :
        Return the binary representation of the input number as a string.
    
    Examples
    --------
    The number 13 is represented by ``00001101``. Likewise, 17 is
    represented by ``00010001``.  The bit-wise XOR of 13 and 17 is
    therefore ``00011100``, or 28:
    
    >>> np.bitwise_xor(13, 17)
    28
    >>> np.binary_repr(28)
    '11100'
    
    >>> np.bitwise_xor(31, 5)
    26
    >>> np.bitwise_xor([31,3], 5)
    array([26,  6])
    
    >>> np.bitwise_xor([31,3], [5,6])
    array([26,  5])
    >>> np.bitwise_xor([True, True], [False, True])
    array([ True, False], dtype=bool)
    """
    pass

def cbrt(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cbrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the cube-root of an array, element-wise.
    
    .. versionadded:: 1.10.0
    
    Parameters
    ----------
    x : array_like
        The values whose cube-roots are required.
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
    y : ndarray
        An array of the same shape as `x`, containing the cube
        cube-root of each element in `x`.
        If `out` was provided, `y` is a reference to it.
    
    
    Examples
    --------
    >>> np.cbrt([1,8,27])
    array([ 1.,  2.,  3.])
    """
    pass

def ceil(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the ceiling of the input, element-wise.
    
    The ceil of the scalar `x` is the smallest integer `i`, such that
    `i >= x`.  It is often denoted as :math:`\lceil x \rceil`.
    
    Parameters
    ----------
    x : array_like
        Input data.
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
    y : ndarray or scalar
        The ceiling of each element in `x`, with `float` dtype.
    
    See Also
    --------
    floor, trunc, rint
    
    Examples
    --------
    >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
    >>> np.ceil(a)
    array([-1., -1., -0.,  1.,  2.,  2.,  2.])
    """
    pass

def conj(*args, **kwargs): # real signature unknown
    """
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the complex conjugate, element-wise.
    
    The complex conjugate of a complex number is obtained by changing the
    sign of its imaginary part.
    
    Parameters
    ----------
    x : array_like
        Input value.
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
    y : ndarray
        The complex conjugate of `x`, with same dtype as `y`.
    
    Examples
    --------
    >>> np.conjugate(1+2j)
    (1-2j)
    
    >>> x = np.eye(2) + 1j * np.eye(2)
    >>> np.conjugate(x)
    array([[ 1.-1.j,  0.-0.j],
           [ 0.-0.j,  1.-1.j]])
    """
    pass

def conjugate(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the complex conjugate, element-wise.
    
    The complex conjugate of a complex number is obtained by changing the
    sign of its imaginary part.
    
    Parameters
    ----------
    x : array_like
        Input value.
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
    y : ndarray
        The complex conjugate of `x`, with same dtype as `y`.
    
    Examples
    --------
    >>> np.conjugate(1+2j)
    (1-2j)
    
    >>> x = np.eye(2) + 1j * np.eye(2)
    >>> np.conjugate(x)
    array([[ 1.-1.j,  0.-0.j],
           [ 0.-0.j,  1.-1.j]])
    """
    pass

def copysign(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    copysign(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Change the sign of x1 to that of x2, element-wise.
    
    If both arguments are arrays or sequences, they have to be of the same
    length. If `x2` is a scalar, its sign will be copied to all elements of
    `x1`.
    
    Parameters
    ----------
    x1 : array_like
        Values to change the sign of.
    x2 : array_like
        The sign of `x2` is copied to `x1`.
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
    out : array_like
        The values of `x1` with the sign of `x2`.
    
    Examples
    --------
    >>> np.copysign(1.3, -1)
    -1.3
    >>> 1/np.copysign(0, 1)
    inf
    >>> 1/np.copysign(0, -1)
    -inf
    
    >>> np.copysign([-1, 0, 1], -1.1)
    array([-1., -0., -1.])
    >>> np.copysign([-1, 0, 1], np.arange(3)-1)
    array([-1.,  0.,  1.])
    """
    pass

def cos(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Cosine element-wise.
    
    Parameters
    ----------
    x : array_like
        Input array in radians.
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
    y : ndarray
        The corresponding cosine values.
    
    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)
    
    References
    ----------
    M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
    New York, NY: Dover, 1972.
    
    Examples
    --------
    >>> np.cos(np.array([0, np.pi/2, np.pi]))
    array([  1.00000000e+00,   6.12303177e-17,  -1.00000000e+00])
    >>>
    >>> # Example of providing the optional output parameter
    >>> out2 = np.cos([0.1], out1)
    >>> out2 is out1
    True
    >>>
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.cos(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid return array shape
    """
    pass

def cosh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Hyperbolic cosine, element-wise.
    
    Equivalent to ``1/2 * (np.exp(x) + np.exp(-x))`` and ``np.cos(1j*x)``.
    
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
    out : ndarray
        Output array of same shape as `x`.
    
    Examples
    --------
    >>> np.cosh(0)
    1.0
    
    The hyperbolic cosine describes the shape of a hanging cable:
    
    >>> import matplotlib.pyplot as plt
    >>> x = np.linspace(-4, 4, 1000)
    >>> plt.plot(x, np.cosh(x))
    >>> plt.show()
    """
    pass

def deg2rad(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    deg2rad(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Convert angles from degrees to radians.
    
    Parameters
    ----------
    x : array_like
        Angles in degrees.
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
    y : ndarray
        The corresponding angle in radians.
    
    See Also
    --------
    rad2deg : Convert angles from radians to degrees.
    unwrap : Remove large jumps in angle by wrapping.
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    ``deg2rad(x)`` is ``x * pi / 180``.
    
    Examples
    --------
    >>> np.deg2rad(180)
    3.1415926535897931
    """
    pass

def degrees(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Convert angles from radians to degrees.
    
    Parameters
    ----------
    x : array_like
        Input array in radians.
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
    y : ndarray of floats
        The corresponding degree values; if `out` was supplied this is a
        reference to it.
    
    See Also
    --------
    rad2deg : equivalent function
    
    Examples
    --------
    Convert a radian array to degrees
    
    >>> rad = np.arange(12.)*np.pi/6
    >>> np.degrees(rad)
    array([   0.,   30.,   60.,   90.,  120.,  150.,  180.,  210.,  240.,
            270.,  300.,  330.])
    
    >>> out = np.zeros((rad.shape))
    >>> r = degrees(rad, out)
    >>> np.all(r == out)
    True
    """
    pass

def divide(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    true_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Returns a true division of the inputs, element-wise.
    
    Instead of the Python traditional 'floor division', this returns a true
    division.  True division adjusts the output type to present the best
    answer, regardless of input types.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
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
    out : ndarray
        Result is scalar if both inputs are scalar, ndarray otherwise.
    
    Notes
    -----
    The floor division operator ``//`` was added in Python 2.2 making
    ``//`` and ``/`` equivalent operators.  The default floor division
    operation of ``/`` can be replaced by true division with ``from
    __future__ import division``.
    
    In Python 3.0, ``//`` is the floor division operator and ``/`` the
    true division operator.  The ``true_divide(x1, x2)`` function is
    equivalent to true division in Python.
    
    Examples
    --------
    >>> x = np.arange(5)
    >>> np.true_divide(x, 4)
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
    
    >>> x/4
    array([0, 0, 0, 0, 1])
    >>> x//4
    array([0, 0, 0, 0, 1])
    
    >>> from __future__ import division
    >>> x/4
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
    >>> x//4
    array([0, 0, 0, 0, 1])
    """
    pass

def divmod(x1, x2, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    divmod(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return element-wise quotient and remainder simultaneously.
    
    .. versionadded:: 1.13.0
    
    ``np.divmod(x, y)`` is equivalent to ``(x // y, x % y)``, but faster
    because it avoids redundant work. It is used to implement the Python
    built-in function ``divmod`` on NumPy arrays.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
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
    out1 : ndarray
        Element-wise quotient resulting from floor division.
    out2 : ndarray
        Element-wise remainder from floor division.
    
    See Also
    --------
    floor_divide : Equivalent to Python's ``//`` operator.
    remainder : Equivalent to Python's ``%`` operator.
    modf : Equivalent to ``divmod(x, 1)`` for positive ``x`` with the return
           values switched.
    
    Examples
    --------
    >>> np.divmod(np.arange(5), 3)
    (array([0, 0, 0, 1, 1]), array([0, 1, 2, 0, 1]))
    """
    pass

def equal(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return (x1 == x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays of the same shape.
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
    out : ndarray or bool
        Output array of bools, or a single bool if x1 and x2 are scalars.
    
    See Also
    --------
    not_equal, greater_equal, less_equal, greater, less
    
    Examples
    --------
    >>> np.equal([0, 1, 3], np.arange(3))
    array([ True,  True, False], dtype=bool)
    
    What is compared are values, not types. So an int (1) and an array of
    length one can evaluate as True:
    
    >>> np.equal(1, np.ones(1))
    array([ True], dtype=bool)
    """
    pass

def exp(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Calculate the exponential of all elements in the input array.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    out : ndarray
        Output array, element-wise exponential of `x`.
    
    See Also
    --------
    expm1 : Calculate ``exp(x) - 1`` for all elements in the array.
    exp2  : Calculate ``2**x`` for all elements in the array.
    
    Notes
    -----
    The irrational number ``e`` is also known as Euler's number.  It is
    approximately 2.718281, and is the base of the natural logarithm,
    ``ln`` (this means that, if :math:`x = \ln y = \log_e y`,
    then :math:`e^x = y`. For real input, ``exp(x)`` is always positive.
    
    For complex arguments, ``x = a + ib``, we can write
    :math:`e^x = e^a e^{ib}`.  The first term, :math:`e^a`, is already
    known (it is the real argument, described above).  The second term,
    :math:`e^{ib}`, is :math:`\cos b + i \sin b`, a function with
    magnitude 1 and a periodic phase.
    
    References
    ----------
    .. [1] Wikipedia, "Exponential function",
           http://en.wikipedia.org/wiki/Exponential_function
    .. [2] M. Abramovitz and I. A. Stegun, "Handbook of Mathematical Functions
           with Formulas, Graphs, and Mathematical Tables," Dover, 1964, p. 69,
           http://www.math.sfu.ca/~cbm/aands/page_69.htm
    
    Examples
    --------
    Plot the magnitude and phase of ``exp(x)`` in the complex plane:
    
    >>> import matplotlib.pyplot as plt
    
    >>> x = np.linspace(-2*np.pi, 2*np.pi, 100)
    >>> xx = x + 1j * x[:, np.newaxis] # a + ib over complex plane
    >>> out = np.exp(xx)
    
    >>> plt.subplot(121)
    >>> plt.imshow(np.abs(out),
    ...            extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='gray')
    >>> plt.title('Magnitude of exp(x)')
    
    >>> plt.subplot(122)
    >>> plt.imshow(np.angle(out),
    ...            extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv')
    >>> plt.title('Phase (angle) of exp(x)')
    >>> plt.show()
    """
    pass

def exp2(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    exp2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Calculate `2**p` for all `p` in the input array.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    out : ndarray
        Element-wise 2 to the power `x`.
    
    See Also
    --------
    power
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    
    
    Examples
    --------
    >>> np.exp2([2, 3])
    array([ 4.,  8.])
    """
    pass

def expm1(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    expm1(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Calculate ``exp(x) - 1`` for all elements in the array.
    
    Parameters
    ----------
    x : array_like
       Input values.
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
    out : ndarray
        Element-wise exponential minus one: ``out = exp(x) - 1``.
    
    See Also
    --------
    log1p : ``log(1 + x)``, the inverse of expm1.
    
    
    Notes
    -----
    This function provides greater precision than ``exp(x) - 1``
    for small values of ``x``.
    
    Examples
    --------
    The true value of ``exp(1e-10) - 1`` is ``1.00000000005e-10`` to
    about 32 significant digits. This example shows the superiority of
    expm1 in this case.
    
    >>> np.expm1(1e-10)
    1.00000000005e-10
    >>> np.exp(1e-10) - 1
    1.000000082740371e-10
    """
    pass

def fabs(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fabs(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the absolute values element-wise.
    
    This function returns the absolute values (positive magnitude) of the
    data in `x`. Complex values are not handled, use `absolute` to find the
    absolute values of complex data.
    
    Parameters
    ----------
    x : array_like
        The array of numbers for which the absolute values are required. If
        `x` is a scalar, the result `y` will also be a scalar.
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
    y : ndarray or scalar
        The absolute values of `x`, the returned values are always floats.
    
    See Also
    --------
    absolute : Absolute values including `complex` types.
    
    Examples
    --------
    >>> np.fabs(-1)
    1.0
    >>> np.fabs([-1.2, 1.2])
    array([ 1.2,  1.2])
    """
    pass

def float_power(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    float_power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    First array elements raised to powers from second array, element-wise.
    
    Raise each base in `x1` to the positionally-corresponding power in `x2`.
    `x1` and `x2` must be broadcastable to the same shape. This differs from
    the power function in that integers, float16, and float32  are promoted to
    floats with a minimum precision of float64 so that the result is always
    inexact.  The intent is that the function will return a usable result for
    negative powers and seldom overflow for positive powers.
    
    .. versionadded:: 1.12.0
    
    Parameters
    ----------
    x1 : array_like
        The bases.
    x2 : array_like
        The exponents.
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
    y : ndarray
        The bases in `x1` raised to the exponents in `x2`.
    
    See Also
    --------
    power : power function that preserves type
    
    Examples
    --------
    Cube each element in a list.
    
    >>> x1 = range(6)
    >>> x1
    [0, 1, 2, 3, 4, 5]
    >>> np.float_power(x1, 3)
    array([   0.,    1.,    8.,   27.,   64.,  125.])
    
    Raise the bases to different exponents.
    
    >>> x2 = [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
    >>> np.float_power(x1, x2)
    array([  0.,   1.,   8.,  27.,  16.,   5.])
    
    The effect of broadcasting.
    
    >>> x2 = np.array([[1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1]])
    >>> x2
    array([[1, 2, 3, 3, 2, 1],
           [1, 2, 3, 3, 2, 1]])
    >>> np.float_power(x1, x2)
    array([[  0.,   1.,   8.,  27.,  16.,   5.],
           [  0.,   1.,   8.,  27.,  16.,   5.]])
    """
    pass

def floor(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the floor of the input, element-wise.
    
    The floor of the scalar `x` is the largest integer `i`, such that
    `i <= x`.  It is often denoted as :math:`\lfloor x \rfloor`.
    
    Parameters
    ----------
    x : array_like
        Input data.
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
    y : ndarray or scalar
        The floor of each element in `x`.
    
    See Also
    --------
    ceil, trunc, rint
    
    Notes
    -----
    Some spreadsheet programs calculate the "floor-towards-zero", in other
    words ``floor(-2.5) == -2``.  NumPy instead uses the definition of
    `floor` where `floor(-2.5) == -3`.
    
    Examples
    --------
    >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
    >>> np.floor(a)
    array([-2., -2., -1.,  0.,  1.,  1.,  2.])
    """
    pass

def floor_divide(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the largest integer smaller or equal to the division of the inputs.
    It is equivalent to the Python ``//`` operator and pairs with the
    Python ``%`` (`remainder`), function so that ``b = a % b + b * (a // b)``
    up to roundoff.
    
    Parameters
    ----------
    x1 : array_like
        Numerator.
    x2 : array_like
        Denominator.
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
    y : ndarray
        y = floor(`x1`/`x2`)
    
    
    See Also
    --------
    remainder : Remainder complementary to floor_divide.
    divmod : Simultaneous floor division and remainder.
    divide : Standard division.
    floor : Round a number to the nearest integer toward minus infinity.
    ceil : Round a number to the nearest integer toward infinity.
    
    Examples
    --------
    >>> np.floor_divide(7,3)
    2
    >>> np.floor_divide([1., 2., 3., 4.], 2.5)
    array([ 0.,  0.,  1.,  1.])
    """
    pass

def fmax(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fmax(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Element-wise maximum of array elements.
    
    Compare two arrays and returns a new array containing the element-wise
    maxima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
    is returned.  The latter distinction is important for complex NaNs,
    which are defined as at least one of the real or imaginary parts being
    a NaN. The net effect is that NaNs are ignored when possible.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared. They must have
        the same shape.
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
    y : ndarray or scalar
        The maximum of `x1` and `x2`, element-wise.  Returns scalar if
        both  `x1` and `x2` are scalars.
    
    See Also
    --------
    fmin :
        Element-wise minimum of two arrays, ignores NaNs.
    maximum :
        Element-wise maximum of two arrays, propagates NaNs.
    amax :
        The maximum value of an array along a given axis, propagates NaNs.
    nanmax :
        The maximum value of an array along a given axis, ignores NaNs.
    
    minimum, amin, nanmin
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    The fmax is equivalent to ``np.where(x1 >= x2, x1, x2)`` when neither
    x1 nor x2 are NaNs, but it is faster and does proper broadcasting.
    
    Examples
    --------
    >>> np.fmax([2, 3, 4], [1, 5, 2])
    array([ 2.,  5.,  4.])
    
    >>> np.fmax(np.eye(2), [0.5, 2])
    array([[ 1. ,  2. ],
           [ 0.5,  2. ]])
    
    >>> np.fmax([np.nan, 0, np.nan],[0, np.nan, np.nan])
    array([  0.,   0.,  NaN])
    """
    pass

def fmin(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fmin(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Element-wise minimum of array elements.
    
    Compare two arrays and returns a new array containing the element-wise
    minima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
    is returned.  The latter distinction is important for complex NaNs,
    which are defined as at least one of the real or imaginary parts being
    a NaN. The net effect is that NaNs are ignored when possible.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared. They must have
        the same shape.
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
    y : ndarray or scalar
        The minimum of `x1` and `x2`, element-wise.  Returns scalar if
        both  `x1` and `x2` are scalars.
    
    See Also
    --------
    fmax :
        Element-wise maximum of two arrays, ignores NaNs.
    minimum :
        Element-wise minimum of two arrays, propagates NaNs.
    amin :
        The minimum value of an array along a given axis, propagates NaNs.
    nanmin :
        The minimum value of an array along a given axis, ignores NaNs.
    
    maximum, amax, nanmax
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    The fmin is equivalent to ``np.where(x1 <= x2, x1, x2)`` when neither
    x1 nor x2 are NaNs, but it is faster and does proper broadcasting.
    
    Examples
    --------
    >>> np.fmin([2, 3, 4], [1, 5, 2])
    array([1, 3, 2])
    
    >>> np.fmin(np.eye(2), [0.5, 2])
    array([[ 0.5,  0. ],
           [ 0. ,  1. ]])
    
    >>> np.fmin([np.nan, 0, np.nan],[0, np.nan, np.nan])
    array([  0.,   0.,  NaN])
    """
    pass

def fmod(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    fmod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the element-wise remainder of division.
    
    This is the NumPy implementation of the C library function fmod, the
    remainder has the same sign as the dividend `x1`. It is equivalent to
    the Matlab(TM) ``rem`` function and should not be confused with the
    Python modulus operator ``x1 % x2``.
    
    Parameters
    ----------
    x1 : array_like
      Dividend.
    x2 : array_like
      Divisor.
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
    y : array_like
      The remainder of the division of `x1` by `x2`.
    
    See Also
    --------
    remainder : Equivalent to the Python ``%`` operator.
    divide
    
    Notes
    -----
    The result of the modulo operation for negative dividend and divisors
    is bound by conventions. For `fmod`, the sign of result is the sign of
    the dividend, while for `remainder` the sign of the result is the sign
    of the divisor. The `fmod` function is equivalent to the Matlab(TM)
    ``rem`` function.
    
    Examples
    --------
    >>> np.fmod([-3, -2, -1, 1, 2, 3], 2)
    array([-1,  0, -1,  1,  0,  1])
    >>> np.remainder([-3, -2, -1, 1, 2, 3], 2)
    array([1, 0, 1, 1, 0, 1])
    
    >>> np.fmod([5, 3], [2, 2.])
    array([ 1.,  1.])
    >>> a = np.arange(-3, 3).reshape(3, 2)
    >>> a
    array([[-3, -2],
           [-1,  0],
           [ 1,  2]])
    >>> np.fmod(a, [2,2])
    array([[-1,  0],
           [-1,  0],
           [ 1,  0]])
    """
    pass

def frexp(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    frexp(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Decompose the elements of x into mantissa and twos exponent.
    
    Returns (`mantissa`, `exponent`), where `x = mantissa * 2**exponent``.
    The mantissa is lies in the open interval(-1, 1), while the twos
    exponent is a signed integer.
    
    Parameters
    ----------
    x : array_like
        Array of numbers to be decomposed.
    out1 : ndarray, optional
        Output array for the mantissa. Must have the same shape as `x`.
    out2 : ndarray, optional
        Output array for the exponent. Must have the same shape as `x`.
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
    (mantissa, exponent) : tuple of ndarrays, (float, int)
        `mantissa` is a float array with values between -1 and 1.
        `exponent` is an int array which represents the exponent of 2.
    
    See Also
    --------
    ldexp : Compute ``y = x1 * 2**x2``, the inverse of `frexp`.
    
    Notes
    -----
    Complex dtypes are not supported, they will raise a TypeError.
    
    Examples
    --------
    >>> x = np.arange(9)
    >>> y1, y2 = np.frexp(x)
    >>> y1
    array([ 0.   ,  0.5  ,  0.5  ,  0.75 ,  0.5  ,  0.625,  0.75 ,  0.875,
            0.5  ])
    >>> y2
    array([0, 1, 2, 2, 3, 3, 3, 3, 4])
    >>> y1 * 2**y2
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.])
    """
    pass

def frompyfunc(func, nin, nout): # real signature unknown; restored from __doc__
    """
    frompyfunc(func, nin, nout)
    
        Takes an arbitrary Python function and returns a NumPy ufunc.
    
        Can be used, for example, to add broadcasting to a built-in Python
        function (see Examples section).
    
        Parameters
        ----------
        func : Python function object
            An arbitrary Python function.
        nin : int
            The number of input arguments.
        nout : int
            The number of objects returned by `func`.
    
        Returns
        -------
        out : ufunc
            Returns a NumPy universal function (``ufunc``) object.
    
        See Also
        --------
        vectorize : evaluates pyfunc over input arrays using broadcasting rules of numpy
    
        Notes
        -----
        The returned ufunc always returns PyObject arrays.
    
        Examples
        --------
        Use frompyfunc to add broadcasting to the Python function ``oct``:
    
        >>> oct_array = np.frompyfunc(oct, 1, 1)
        >>> oct_array(np.array((10, 30, 100)))
        array([012, 036, 0144], dtype=object)
        >>> np.array((oct(10), oct(30), oct(100))) # for comparison
        array(['012', '036', '0144'],
              dtype='|S4')
    """
    pass

def geterrobj(): # real signature unknown; restored from __doc__
    """
    geterrobj()
    
        Return the current object that defines floating-point error handling.
    
        The error object contains all information that defines the error handling
        behavior in NumPy. `geterrobj` is used internally by the other
        functions that get and set error handling behavior (`geterr`, `seterr`,
        `geterrcall`, `seterrcall`).
    
        Returns
        -------
        errobj : list
            The error object, a list containing three elements:
            [internal numpy buffer size, error mask, error callback function].
    
            The error mask is a single integer that holds the treatment information
            on all four floating point errors. The information for each error type
            is contained in three bits of the integer. If we print it in base 8, we
            can see what treatment is set for "invalid", "under", "over", and
            "divide" (in that order). The printed string can be interpreted with
    
            * 0 : 'ignore'
            * 1 : 'warn'
            * 2 : 'raise'
            * 3 : 'call'
            * 4 : 'print'
            * 5 : 'log'
    
        See Also
        --------
        seterrobj, seterr, geterr, seterrcall, geterrcall
        getbufsize, setbufsize
    
        Notes
        -----
        For complete documentation of the types of floating-point exceptions and
        treatment options, see `seterr`.
    
        Examples
        --------
        >>> np.geterrobj()  # first get the defaults
        [10000, 0, None]
    
        >>> def err_handler(type, flag):
        ...     print("Floating point error (%s), with flag %s" % (type, flag))
        ...
        >>> old_bufsize = np.setbufsize(20000)
        >>> old_err = np.seterr(divide='raise')
        >>> old_handler = np.seterrcall(err_handler)
        >>> np.geterrobj()
        [20000, 2, <function err_handler at 0x91dcaac>]
    
        >>> old_err = np.seterr(all='ignore')
        >>> np.base_repr(np.geterrobj()[1], 8)
        '0'
        >>> old_err = np.seterr(divide='warn', over='log', under='call',
                                invalid='print')
        >>> np.base_repr(np.geterrobj()[1], 8)
        '4351'
    """
    pass

def greater(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the truth value of (x1 > x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays.  If ``x1.shape != x2.shape``, they must be
        broadcastable to a common shape (which may be the shape of one or
        the other).
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
    out : bool or ndarray of bool
        Array of bools, or a single bool if `x1` and `x2` are scalars.
    
    
    See Also
    --------
    greater_equal, less, less_equal, equal, not_equal
    
    Examples
    --------
    >>> np.greater([4,2],[2,2])
    array([ True, False], dtype=bool)
    
    If the inputs are ndarrays, then np.greater is equivalent to '>'.
    
    >>> a = np.array([4,2])
    >>> b = np.array([2,2])
    >>> a > b
    array([ True, False], dtype=bool)
    """
    pass

def greater_equal(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the truth value of (x1 >= x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays.  If ``x1.shape != x2.shape``, they must be
        broadcastable to a common shape (which may be the shape of one or
        the other).
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
    out : bool or ndarray of bool
        Array of bools, or a single bool if `x1` and `x2` are scalars.
    
    See Also
    --------
    greater, less, less_equal, equal, not_equal
    
    Examples
    --------
    >>> np.greater_equal([4, 2, 1], [2, 2, 2])
    array([ True, True, False], dtype=bool)
    """
    pass

def heaviside(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    heaviside(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the Heaviside step function.
    
    The Heaviside step function is defined as::
    
                              0   if x1 < 0
        heaviside(x1, x2) =  x2   if x1 == 0
                              1   if x1 > 0
    
    where `x2` is often taken to be 0.5, but 0 and 1 are also sometimes used.
    
    Parameters
    ----------
    x1 : array_like
        Input values.
    x2 : array_like
        The value of the function when x1 is 0.
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
    out : ndarray
        The output array, element-wise Heaviside step function of `x1`.
    
    Notes
    -----
    .. versionadded:: 1.13.0
    
    References
    ----------
    .. Wikipedia, "Heaviside step function",
       https://en.wikipedia.org/wiki/Heaviside_step_function
    
    Examples
    --------
    >>> np.heaviside([-1.5, 0, 2.0], 0.5)
    array([ 0. ,  0.5,  1. ])
    >>> np.heaviside([-1.5, 0, 2.0], 1)
    array([ 0.,  1.,  1.])
    """
    pass

def hypot(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    hypot(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Given the "legs" of a right triangle, return its hypotenuse.
    
    Equivalent to ``sqrt(x1**2 + x2**2)``, element-wise.  If `x1` or
    `x2` is scalar_like (i.e., unambiguously cast-able to a scalar type),
    it is broadcast for use with each element of the other argument.
    (See Examples)
    
    Parameters
    ----------
    x1, x2 : array_like
        Leg of the triangle(s).
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
    z : ndarray
        The hypotenuse of the triangle(s).
    
    Examples
    --------
    >>> np.hypot(3*np.ones((3, 3)), 4*np.ones((3, 3)))
    array([[ 5.,  5.,  5.],
           [ 5.,  5.,  5.],
           [ 5.,  5.,  5.]])
    
    Example showing broadcast of scalar_like argument:
    
    >>> np.hypot(3*np.ones((3, 3)), [4])
    array([[ 5.,  5.,  5.],
           [ 5.,  5.,  5.],
           [ 5.,  5.,  5.]])
    """
    pass

def invert(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute bit-wise inversion, or bit-wise NOT, element-wise.
    
    Computes the bit-wise NOT of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``~``.
    
    For signed integer inputs, the two's complement is returned.  In a
    two's-complement system negative numbers are represented by the two's
    complement of the absolute value. This is the most common method of
    representing signed integers on computers [1]_. A N-bit
    two's-complement system can represent every integer in the range
    :math:`-2^{N-1}` to :math:`+2^{N-1}-1`.
    
    Parameters
    ----------
    x : array_like
        Only integer and boolean types are handled.
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
    out : array_like
        Result.
    
    See Also
    --------
    bitwise_and, bitwise_or, bitwise_xor
    logical_not
    binary_repr :
        Return the binary representation of the input number as a string.
    
    Notes
    -----
    `bitwise_not` is an alias for `invert`:
    
    >>> np.bitwise_not is np.invert
    True
    
    References
    ----------
    .. [1] Wikipedia, "Two's complement",
        http://en.wikipedia.org/wiki/Two's_complement
    
    Examples
    --------
    We've seen that 13 is represented by ``00001101``.
    The invert or bit-wise NOT of 13 is then:
    
    >>> np.invert(np.array([13], dtype=uint8))
    array([242], dtype=uint8)
    >>> np.binary_repr(x, width=8)
    '00001101'
    >>> np.binary_repr(242, width=8)
    '11110010'
    
    The result depends on the bit-width:
    
    >>> np.invert(np.array([13], dtype=uint16))
    array([65522], dtype=uint16)
    >>> np.binary_repr(x, width=16)
    '0000000000001101'
    >>> np.binary_repr(65522, width=16)
    '1111111111110010'
    
    When using signed integer types the result is the two's complement of
    the result for the unsigned type:
    
    >>> np.invert(np.array([13], dtype=int8))
    array([-14], dtype=int8)
    >>> np.binary_repr(-14, width=8)
    '11110010'
    
    Booleans are accepted as well:
    
    >>> np.invert(array([True, False]))
    array([False,  True], dtype=bool)
    """
    pass

def isfinite(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Test element-wise for finiteness (not infinity or not Not a Number).
    
    The result is returned as a boolean array.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    y : ndarray, bool
        For scalar input, the result is a new boolean with value True
        if the input is finite; otherwise the value is False (input is
        either positive infinity, negative infinity or Not a Number).
    
        For array input, the result is a boolean array with the same
        dimensions as the input and the values are True if the
        corresponding element of the input is finite; otherwise the values
        are False (element is either positive infinity, negative infinity
        or Not a Number).
    
    See Also
    --------
    isinf, isneginf, isposinf, isnan
    
    Notes
    -----
    Not a Number, positive infinity and negative infinity are considered
    to be non-finite.
    
    NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754). This means that Not a Number is not equivalent to infinity.
    Also that positive infinity is not equivalent to negative infinity. But
    infinity is equivalent to positive infinity.  Errors result if the
    second argument is also supplied when `x` is a scalar input, or if
    first and second arguments have different shapes.
    
    Examples
    --------
    >>> np.isfinite(1)
    True
    >>> np.isfinite(0)
    True
    >>> np.isfinite(np.nan)
    False
    >>> np.isfinite(np.inf)
    False
    >>> np.isfinite(np.NINF)
    False
    >>> np.isfinite([np.log(-1.),1.,np.log(0)])
    array([False,  True, False], dtype=bool)
    
    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isfinite(x, y)
    array([0, 1, 0])
    >>> y
    array([0, 1, 0])
    """
    pass

def isinf(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Test element-wise for positive or negative infinity.
    
    Returns a boolean array of the same shape as `x`, True where ``x ==
    +/-inf``, otherwise False.
    
    Parameters
    ----------
    x : array_like
        Input values
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
    y : bool (scalar) or boolean ndarray
        For scalar input, the result is a new boolean with value True if
        the input is positive or negative infinity; otherwise the value is
        False.
    
        For array input, the result is a boolean array with the same shape
        as the input and the values are True where the corresponding
        element of the input is positive or negative infinity; elsewhere
        the values are False.  If a second argument was supplied the result
        is stored there.  If the type of that array is a numeric type the
        result is represented as zeros and ones, if the type is boolean
        then as False and True, respectively.  The return value `y` is then
        a reference to that array.
    
    See Also
    --------
    isneginf, isposinf, isnan, isfinite
    
    Notes
    -----
    NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754).
    
    Errors result if the second argument is supplied when the first
    argument is a scalar, or if the first and second arguments have
    different shapes.
    
    Examples
    --------
    >>> np.isinf(np.inf)
    True
    >>> np.isinf(np.nan)
    False
    >>> np.isinf(np.NINF)
    True
    >>> np.isinf([np.inf, -np.inf, 1.0, np.nan])
    array([ True,  True, False, False], dtype=bool)
    
    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isinf(x, y)
    array([1, 0, 1])
    >>> y
    array([1, 0, 1])
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

def isnat(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    isnat(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Test element-wise for NaT (not a time) and return result as a boolean array.
    
    Parameters
    ----------
    x : array_like
        Input array with datetime or timedelta data type.
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
        the input is NaT; otherwise the value is False.
    
        For array input, the result is a boolean array of the same
        dimensions as the input and the values are True if the
        corresponding element of the input is NaT; otherwise the values are
        False.
    
    See Also
    --------
    isnan, isinf, isneginf, isposinf, isfinite
    
    Examples
    --------
    >>> np.isnat(np.datetime64("NaT"))
    True
    >>> np.isnat(np.datetime64("2016-01-01"))
    False
    >>> np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]"))
    array([ True, False], dtype=bool)
    """
    pass

def ldexp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    ldexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Returns x1 * 2**x2, element-wise.
    
    The mantissas `x1` and twos exponents `x2` are used to construct
    floating point numbers ``x1 * 2**x2``.
    
    Parameters
    ----------
    x1 : array_like
        Array of multipliers.
    x2 : array_like, int
        Array of twos exponents.
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
    y : ndarray or scalar
        The result of ``x1 * 2**x2``.
    
    See Also
    --------
    frexp : Return (y1, y2) from ``x = y1 * 2**y2``, inverse to `ldexp`.
    
    Notes
    -----
    Complex dtypes are not supported, they will raise a TypeError.
    
    `ldexp` is useful as the inverse of `frexp`, if used by itself it is
    more clear to simply use the expression ``x1 * 2**x2``.
    
    Examples
    --------
    >>> np.ldexp(5, np.arange(4))
    array([  5.,  10.,  20.,  40.], dtype=float32)
    
    >>> x = np.arange(6)
    >>> np.ldexp(*np.frexp(x))
    array([ 0.,  1.,  2.,  3.,  4.,  5.])
    """
    pass

def left_shift(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Shift the bits of an integer to the left.
    
    Bits are shifted to the left by appending `x2` 0s at the right of `x1`.
    Since the internal representation of numbers is in binary format, this
    operation is equivalent to multiplying `x1` by ``2**x2``.
    
    Parameters
    ----------
    x1 : array_like of integer type
        Input values.
    x2 : array_like of integer type
        Number of zeros to append to `x1`. Has to be non-negative.
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
    out : array of integer type
        Return `x1` with bits shifted `x2` times to the left.
    
    See Also
    --------
    right_shift : Shift the bits of an integer to the right.
    binary_repr : Return the binary representation of the input number
        as a string.
    
    Examples
    --------
    >>> np.binary_repr(5)
    '101'
    >>> np.left_shift(5, 2)
    20
    >>> np.binary_repr(20)
    '10100'
    
    >>> np.left_shift(5, [1,2,3])
    array([10, 20, 40])
    """
    pass

def less(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the truth value of (x1 < x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays.  If ``x1.shape != x2.shape``, they must be
        broadcastable to a common shape (which may be the shape of one or
        the other).
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
    out : bool or ndarray of bool
        Array of bools, or a single bool if `x1` and `x2` are scalars.
    
    See Also
    --------
    greater, less_equal, greater_equal, equal, not_equal
    
    Examples
    --------
    >>> np.less([1, 2], [2, 2])
    array([ True, False], dtype=bool)
    """
    pass

def less_equal(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the truth value of (x1 =< x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays.  If ``x1.shape != x2.shape``, they must be
        broadcastable to a common shape (which may be the shape of one or
        the other).
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
    out : bool or ndarray of bool
        Array of bools, or a single bool if `x1` and `x2` are scalars.
    
    See Also
    --------
    greater, less, greater_equal, equal, not_equal
    
    Examples
    --------
    >>> np.less_equal([4, 2, 1], [2, 2, 2])
    array([False,  True,  True], dtype=bool)
    """
    pass

def log(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Natural logarithm, element-wise.
    
    The natural logarithm `log` is the inverse of the exponential function,
    so that `log(exp(x)) = x`. The natural logarithm is logarithm in base
    `e`.
    
    Parameters
    ----------
    x : array_like
        Input value.
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
    y : ndarray
        The natural logarithm of `x`, element-wise.
    
    See Also
    --------
    log10, log2, log1p, emath.log
    
    Notes
    -----
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `exp(z) = x`. The convention is to return the
    `z` whose imaginary part lies in `[-pi, pi]`.
    
    For real-valued input data types, `log` always returns real output. For
    each value that cannot be expressed as a real number or infinity, it
    yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `log` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it. `log`
    handles the floating-point negative zero as an infinitesimal negative
    number, conforming to the C99 standard.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Logarithm". http://en.wikipedia.org/wiki/Logarithm
    
    Examples
    --------
    >>> np.log([1, np.e, np.e**2, 0])
    array([  0.,   1.,   2., -Inf])
    """
    pass

def log10(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the base 10 logarithm of the input array, element-wise.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    y : ndarray
        The logarithm to the base 10 of `x`, element-wise. NaNs are
        returned where x is negative.
    
    See Also
    --------
    emath.log10
    
    Notes
    -----
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `10**z = x`. The convention is to return the
    `z` whose imaginary part lies in `[-pi, pi]`.
    
    For real-valued input data types, `log10` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `log10` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it.
    `log10` handles the floating-point negative zero as an infinitesimal
    negative number, conforming to the C99 standard.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Logarithm". http://en.wikipedia.org/wiki/Logarithm
    
    Examples
    --------
    >>> np.log10([1e-15, -3.])
    array([-15.,  NaN])
    """
    pass

def log1p(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    log1p(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the natural logarithm of one plus the input array, element-wise.
    
    Calculates ``log(1 + x)``.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    y : ndarray
        Natural logarithm of `1 + x`, element-wise.
    
    See Also
    --------
    expm1 : ``exp(x) - 1``, the inverse of `log1p`.
    
    Notes
    -----
    For real-valued input, `log1p` is accurate also for `x` so small
    that `1 + x == 1` in floating-point accuracy.
    
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `exp(z) = 1 + x`. The convention is to return
    the `z` whose imaginary part lies in `[-pi, pi]`.
    
    For real-valued input data types, `log1p` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `log1p` is a complex analytical function that
    has a branch cut `[-inf, -1]` and is continuous from above on it.
    `log1p` handles the floating-point negative zero as an infinitesimal
    negative number, conforming to the C99 standard.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Logarithm". http://en.wikipedia.org/wiki/Logarithm
    
    Examples
    --------
    >>> np.log1p(1e-99)
    1e-99
    >>> np.log(1 + 1e-99)
    0.0
    """
    pass

def log2(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    log2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Base-2 logarithm of `x`.
    
    Parameters
    ----------
    x : array_like
        Input values.
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
    y : ndarray
        Base-2 logarithm of `x`.
    
    See Also
    --------
    log, log10, log1p, emath.log2
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `2**z = x`. The convention is to return the `z`
    whose imaginary part lies in `[-pi, pi]`.
    
    For real-valued input data types, `log2` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `log2` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it. `log2`
    handles the floating-point negative zero as an infinitesimal negative
    number, conforming to the C99 standard.
    
    Examples
    --------
    >>> x = np.array([0, 1, 2, 2**4])
    >>> np.log2(x)
    array([-Inf,   0.,   1.,   4.])
    
    >>> xi = np.array([0+1.j, 1, 2+0.j, 4.j])
    >>> np.log2(xi)
    array([ 0.+2.26618007j,  0.+0.j        ,  1.+0.j        ,  2.+2.26618007j])
    """
    pass

def logaddexp(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logaddexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Logarithm of the sum of exponentiations of the inputs.
    
    Calculates ``log(exp(x1) + exp(x2))``. This function is useful in
    statistics where the calculated probabilities of events may be so small
    as to exceed the range of normal floating point numbers.  In such cases
    the logarithm of the calculated probability is stored. This function
    allows adding probabilities stored in such a fashion.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input values.
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
    result : ndarray
        Logarithm of ``exp(x1) + exp(x2)``.
    
    See Also
    --------
    logaddexp2: Logarithm of the sum of exponentiations of inputs in base 2.
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    Examples
    --------
    >>> prob1 = np.log(1e-50)
    >>> prob2 = np.log(2.5e-50)
    >>> prob12 = np.logaddexp(prob1, prob2)
    >>> prob12
    -113.87649168120691
    >>> np.exp(prob12)
    3.5000000000000057e-50
    """
    pass

def logaddexp2(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logaddexp2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Logarithm of the sum of exponentiations of the inputs in base-2.
    
    Calculates ``log2(2**x1 + 2**x2)``. This function is useful in machine
    learning when the calculated probabilities of events may be so small as
    to exceed the range of normal floating point numbers.  In such cases
    the base-2 logarithm of the calculated probability can be used instead.
    This function allows adding probabilities stored in such a fashion.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input values.
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
    result : ndarray
        Base-2 logarithm of ``2**x1 + 2**x2``.
    
    See Also
    --------
    logaddexp: Logarithm of the sum of exponentiations of the inputs.
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    Examples
    --------
    >>> prob1 = np.log2(1e-50)
    >>> prob2 = np.log2(2.5e-50)
    >>> prob12 = np.logaddexp2(prob1, prob2)
    >>> prob1, prob2, prob12
    (-166.09640474436813, -164.77447664948076, -164.28904982231052)
    >>> 2**prob12
    3.4999999999999914e-50
    """
    pass

def logical_and(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logical_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the truth value of x1 AND x2 element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays. `x1` and `x2` must be of the same shape.
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
        Boolean result with the same shape as `x1` and `x2` of the logical
        AND operation on corresponding elements of `x1` and `x2`.
    
    See Also
    --------
    logical_or, logical_not, logical_xor
    bitwise_and
    
    Examples
    --------
    >>> np.logical_and(True, False)
    False
    >>> np.logical_and([True, False], [False, False])
    array([False, False], dtype=bool)
    
    >>> x = np.arange(5)
    >>> np.logical_and(x>1, x<4)
    array([False, False,  True,  True, False], dtype=bool)
    """
    pass

def logical_not(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logical_not(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the truth value of NOT x element-wise.
    
    Parameters
    ----------
    x : array_like
        Logical NOT is applied to the elements of `x`.
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
    y : bool or ndarray of bool
        Boolean result with the same shape as `x` of the NOT operation
        on elements of `x`.
    
    See Also
    --------
    logical_and, logical_or, logical_xor
    
    Examples
    --------
    >>> np.logical_not(3)
    False
    >>> np.logical_not([True, False, 0, 1])
    array([False,  True,  True, False], dtype=bool)
    
    >>> x = np.arange(5)
    >>> np.logical_not(x<3)
    array([False, False, False,  True,  True], dtype=bool)
    """
    pass

def logical_or(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logical_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the truth value of x1 OR x2 element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Logical OR is applied to the elements of `x1` and `x2`.
        They have to be of the same shape.
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
        Boolean result with the same shape as `x1` and `x2` of the logical
        OR operation on elements of `x1` and `x2`.
    
    See Also
    --------
    logical_and, logical_not, logical_xor
    bitwise_or
    
    Examples
    --------
    >>> np.logical_or(True, False)
    True
    >>> np.logical_or([True, False], [False, False])
    array([ True, False], dtype=bool)
    
    >>> x = np.arange(5)
    >>> np.logical_or(x < 1, x > 3)
    array([ True, False, False, False,  True], dtype=bool)
    """
    pass

def logical_xor(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute the truth value of x1 XOR x2, element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Logical XOR is applied to the elements of `x1` and `x2`.  They must
        be broadcastable to the same shape.
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
    y : bool or ndarray of bool
        Boolean result of the logical XOR operation applied to the elements
        of `x1` and `x2`; the shape is determined by whether or not
        broadcasting of one or both arrays was required.
    
    See Also
    --------
    logical_and, logical_or, logical_not, bitwise_xor
    
    Examples
    --------
    >>> np.logical_xor(True, False)
    True
    >>> np.logical_xor([True, True, False, False], [True, False, True, False])
    array([False,  True,  True, False], dtype=bool)
    
    >>> x = np.arange(5)
    >>> np.logical_xor(x < 1, x > 3)
    array([ True, False, False, False,  True], dtype=bool)
    
    Simple example showing support of broadcasting
    
    >>> np.logical_xor(0, np.eye(2))
    array([[ True, False],
           [False,  True]], dtype=bool)
    """
    pass

def maximum(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Element-wise maximum of array elements.
    
    Compare two arrays and returns a new array containing the element-wise
    maxima. If one of the elements being compared is a NaN, then that
    element is returned. If both elements are NaNs then the first is
    returned. The latter distinction is important for complex NaNs, which
    are defined as at least one of the real or imaginary parts being a NaN.
    The net effect is that NaNs are propagated.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared. They must have
        the same shape, or shapes that can be broadcast to a single shape.
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
    y : ndarray or scalar
        The maximum of `x1` and `x2`, element-wise.  Returns scalar if
        both  `x1` and `x2` are scalars.
    
    See Also
    --------
    minimum :
        Element-wise minimum of two arrays, propagates NaNs.
    fmax :
        Element-wise maximum of two arrays, ignores NaNs.
    amax :
        The maximum value of an array along a given axis, propagates NaNs.
    nanmax :
        The maximum value of an array along a given axis, ignores NaNs.
    
    fmin, amin, nanmin
    
    Notes
    -----
    The maximum is equivalent to ``np.where(x1 >= x2, x1, x2)`` when
    neither x1 nor x2 are nans, but it is faster and does proper
    broadcasting.
    
    Examples
    --------
    >>> np.maximum([2, 3, 4], [1, 5, 2])
    array([2, 5, 4])
    
    >>> np.maximum(np.eye(2), [0.5, 2]) # broadcasting
    array([[ 1. ,  2. ],
           [ 0.5,  2. ]])
    
    >>> np.maximum([np.nan, 0, np.nan], [0, np.nan, np.nan])
    array([ NaN,  NaN,  NaN])
    >>> np.maximum(np.Inf, 1)
    inf
    """
    pass

def minimum(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Element-wise minimum of array elements.
    
    Compare two arrays and returns a new array containing the element-wise
    minima. If one of the elements being compared is a NaN, then that
    element is returned. If both elements are NaNs then the first is
    returned. The latter distinction is important for complex NaNs, which
    are defined as at least one of the real or imaginary parts being a NaN.
    The net effect is that NaNs are propagated.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared. They must have
        the same shape, or shapes that can be broadcast to a single shape.
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
    y : ndarray or scalar
        The minimum of `x1` and `x2`, element-wise.  Returns scalar if
        both  `x1` and `x2` are scalars.
    
    See Also
    --------
    maximum :
        Element-wise maximum of two arrays, propagates NaNs.
    fmin :
        Element-wise minimum of two arrays, ignores NaNs.
    amin :
        The minimum value of an array along a given axis, propagates NaNs.
    nanmin :
        The minimum value of an array along a given axis, ignores NaNs.
    
    fmax, amax, nanmax
    
    Notes
    -----
    The minimum is equivalent to ``np.where(x1 <= x2, x1, x2)`` when
    neither x1 nor x2 are NaNs, but it is faster and does proper
    broadcasting.
    
    Examples
    --------
    >>> np.minimum([2, 3, 4], [1, 5, 2])
    array([1, 3, 2])
    
    >>> np.minimum(np.eye(2), [0.5, 2]) # broadcasting
    array([[ 0.5,  0. ],
           [ 0. ,  1. ]])
    
    >>> np.minimum([np.nan, 0, np.nan],[0, np.nan, np.nan])
    array([ NaN,  NaN,  NaN])
    >>> np.minimum(-np.Inf, 1)
    -inf
    """
    pass

def mod(*args, **kwargs): # real signature unknown
    """
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return element-wise remainder of division.
    
    Computes the remainder complementary to the `floor_divide` function.  It is
    equivalent to the Python modulus operator``x1 % x2`` and has the same sign
    as the divisor `x2`. It should not be confused with the Matlab(TM) ``rem``
    function.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
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
    y : ndarray
        The element-wise remainder of the quotient ``floor_divide(x1, x2)``.
        Returns a scalar if both  `x1` and `x2` are scalars.
    
    See Also
    --------
    floor_divide : Equivalent of Python ``//`` operator.
    divmod : Simultaneous floor division and remainder.
    fmod : Equivalent of the Matlab(TM) ``rem`` function.
    divide, floor
    
    Notes
    -----
    Returns 0 when `x2` is 0 and both `x1` and `x2` are (arrays of)
    integers.
    
    Examples
    --------
    >>> np.remainder([4, 7], [2, 3])
    array([0, 1])
    >>> np.remainder(np.arange(7), 5)
    array([0, 1, 2, 3, 4, 0, 1])
    """
    pass

def modf(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    modf(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the fractional and integral parts of an array, element-wise.
    
    The fractional and integral parts are negative if the given number is
    negative.
    
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
    y1 : ndarray
        Fractional part of `x`.
    y2 : ndarray
        Integral part of `x`.
    
    Notes
    -----
    For integer input the return values are floats.
    
    See Also
    --------
    divmod : ``divmod(x, 1)`` is equivalent to ``modf`` with the return values
             switched, except it always has a positive remainder.
    
    Examples
    --------
    >>> np.modf([0, 3.5])
    (array([ 0. ,  0.5]), array([ 0.,  3.]))
    >>> np.modf(-0.5)
    (-0.5, -0)
    """
    pass

def multiply(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Multiply arguments element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        Input arrays to be multiplied.
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
    y : ndarray
        The product of `x1` and `x2`, element-wise. Returns a scalar if
        both  `x1` and `x2` are scalars.
    
    Notes
    -----
    Equivalent to `x1` * `x2` in terms of array broadcasting.
    
    Examples
    --------
    >>> np.multiply(2.0, 4.0)
    8.0
    
    >>> x1 = np.arange(9.0).reshape((3, 3))
    >>> x2 = np.arange(3.0)
    >>> np.multiply(x1, x2)
    array([[  0.,   1.,   4.],
           [  0.,   4.,  10.],
           [  0.,   7.,  16.]])
    """
    pass

def negative(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Numerical negative, element-wise.
    
    Parameters
    ----------
    x : array_like or scalar
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
    y : ndarray or scalar
        Returned array or scalar: `y = -x`.
    
    Examples
    --------
    >>> np.negative([1.,-1.])
    array([-1.,  1.])
    """
    pass

def nextafter(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    nextafter(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the next floating-point value after x1 towards x2, element-wise.
    
    Parameters
    ----------
    x1 : array_like
        Values to find the next representable value of.
    x2 : array_like
        The direction where to look for the next representable value of `x1`.
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
    out : array_like
        The next representable values of `x1` in the direction of `x2`.
    
    Examples
    --------
    >>> eps = np.finfo(np.float64).eps
    >>> np.nextafter(1, 2) == eps + 1
    True
    >>> np.nextafter([1, 2], [2, 1]) == [eps + 1, 2 - eps]
    array([ True,  True], dtype=bool)
    """
    pass

def not_equal(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return (x1 != x2) element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
      Input arrays.
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
    not_equal : ndarray bool, scalar bool
      For each element in `x1, x2`, return True if `x1` is not equal
      to `x2` and False otherwise.
    
    
    See Also
    --------
    equal, greater, greater_equal, less, less_equal
    
    Examples
    --------
    >>> np.not_equal([1.,2.], [1., 3.])
    array([False,  True], dtype=bool)
    >>> np.not_equal([1, 2], [[1, 3],[1, 4]])
    array([[False,  True],
           [False,  True]], dtype=bool)
    """
    pass

def positive(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Numerical positive, element-wise.
    
    .. versionadded:: 1.13.0
    
    Parameters
    ----------
    x : array_like or scalar
        Input array.
    
    Returns
    -------
    y : ndarray or scalar
        Returned array or scalar: `y = +x`.
    
    Notes
    -----
    Equivalent to `x.copy()`, but only defined for types that support
    arithmetic.
    """
    pass

def power(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    First array elements raised to powers from second array, element-wise.
    
    Raise each base in `x1` to the positionally-corresponding power in
    `x2`.  `x1` and `x2` must be broadcastable to the same shape. Note that an
    integer type raised to a negative integer power will raise a ValueError.
    
    Parameters
    ----------
    x1 : array_like
        The bases.
    x2 : array_like
        The exponents.
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
    y : ndarray
        The bases in `x1` raised to the exponents in `x2`.
    
    See Also
    --------
    float_power : power function that promotes integers to float
    
    Examples
    --------
    Cube each element in a list.
    
    >>> x1 = range(6)
    >>> x1
    [0, 1, 2, 3, 4, 5]
    >>> np.power(x1, 3)
    array([  0,   1,   8,  27,  64, 125])
    
    Raise the bases to different exponents.
    
    >>> x2 = [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
    >>> np.power(x1, x2)
    array([  0.,   1.,   8.,  27.,  16.,   5.])
    
    The effect of broadcasting.
    
    >>> x2 = np.array([[1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1]])
    >>> x2
    array([[1, 2, 3, 3, 2, 1],
           [1, 2, 3, 3, 2, 1]])
    >>> np.power(x1, x2)
    array([[ 0,  1,  8, 27, 16,  5],
           [ 0,  1,  8, 27, 16,  5]])
    """
    pass

def rad2deg(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rad2deg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Convert angles from radians to degrees.
    
    Parameters
    ----------
    x : array_like
        Angle in radians.
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
    y : ndarray
        The corresponding angle in degrees.
    
    See Also
    --------
    deg2rad : Convert angles from degrees to radians.
    unwrap : Remove large jumps in angle by wrapping.
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    rad2deg(x) is ``180 * x / pi``.
    
    Examples
    --------
    >>> np.rad2deg(np.pi/2)
    90.0
    """
    pass

def radians(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Convert angles from degrees to radians.
    
    Parameters
    ----------
    x : array_like
        Input array in degrees.
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
    y : ndarray
        The corresponding radian values.
    
    See Also
    --------
    deg2rad : equivalent function
    
    Examples
    --------
    Convert a degree array to radians
    
    >>> deg = np.arange(12.) * 30.
    >>> np.radians(deg)
    array([ 0.        ,  0.52359878,  1.04719755,  1.57079633,  2.0943951 ,
            2.61799388,  3.14159265,  3.66519143,  4.1887902 ,  4.71238898,
            5.23598776,  5.75958653])
    
    >>> out = np.zeros((deg.shape))
    >>> ret = np.radians(deg, out)
    >>> ret is out
    True
    """
    pass

def reciprocal(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the reciprocal of the argument, element-wise.
    
    Calculates ``1/x``.
    
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
    y : ndarray
        Return array.
    
    Notes
    -----
    .. note::
        This function is not designed to work with integers.
    
    For integer arguments with absolute value larger than 1 the result is
    always zero because of the way Python handles integer division.  For
    integer zero the result is an overflow.
    
    Examples
    --------
    >>> np.reciprocal(2.)
    0.5
    >>> np.reciprocal([1, 2., 3.33])
    array([ 1.       ,  0.5      ,  0.3003003])
    """
    pass

def remainder(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return element-wise remainder of division.
    
    Computes the remainder complementary to the `floor_divide` function.  It is
    equivalent to the Python modulus operator``x1 % x2`` and has the same sign
    as the divisor `x2`. It should not be confused with the Matlab(TM) ``rem``
    function.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
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
    y : ndarray
        The element-wise remainder of the quotient ``floor_divide(x1, x2)``.
        Returns a scalar if both  `x1` and `x2` are scalars.
    
    See Also
    --------
    floor_divide : Equivalent of Python ``//`` operator.
    divmod : Simultaneous floor division and remainder.
    fmod : Equivalent of the Matlab(TM) ``rem`` function.
    divide, floor
    
    Notes
    -----
    Returns 0 when `x2` is 0 and both `x1` and `x2` are (arrays of)
    integers.
    
    Examples
    --------
    >>> np.remainder([4, 7], [2, 3])
    array([0, 1])
    >>> np.remainder(np.arange(7), 5)
    array([0, 1, 2, 3, 4, 0, 1])
    """
    pass

def right_shift(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Shift the bits of an integer to the right.
    
    Bits are shifted to the right `x2`.  Because the internal
    representation of numbers is in binary format, this operation is
    equivalent to dividing `x1` by ``2**x2``.
    
    Parameters
    ----------
    x1 : array_like, int
        Input values.
    x2 : array_like, int
        Number of bits to remove at the right of `x1`.
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
    out : ndarray, int
        Return `x1` with bits shifted `x2` times to the right.
    
    See Also
    --------
    left_shift : Shift the bits of an integer to the left.
    binary_repr : Return the binary representation of the input number
        as a string.
    
    Examples
    --------
    >>> np.binary_repr(10)
    '1010'
    >>> np.right_shift(10, 1)
    5
    >>> np.binary_repr(5)
    '101'
    
    >>> np.right_shift(10, [1,2,3])
    array([5, 2, 1])
    """
    pass

def rint(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rint(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Round elements of the array to the nearest integer.
    
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
    out : ndarray or scalar
        Output array is same shape and type as `x`.
    
    See Also
    --------
    ceil, floor, trunc
    
    Examples
    --------
    >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
    >>> np.rint(a)
    array([-2., -2., -0.,  0.,  2.,  2.,  2.])
    """
    pass

def seterrobj(errobj): # real signature unknown; restored from __doc__
    """
    seterrobj(errobj)
    
        Set the object that defines floating-point error handling.
    
        The error object contains all information that defines the error handling
        behavior in NumPy. `seterrobj` is used internally by the other
        functions that set error handling behavior (`seterr`, `seterrcall`).
    
        Parameters
        ----------
        errobj : list
            The error object, a list containing three elements:
            [internal numpy buffer size, error mask, error callback function].
    
            The error mask is a single integer that holds the treatment information
            on all four floating point errors. The information for each error type
            is contained in three bits of the integer. If we print it in base 8, we
            can see what treatment is set for "invalid", "under", "over", and
            "divide" (in that order). The printed string can be interpreted with
    
            * 0 : 'ignore'
            * 1 : 'warn'
            * 2 : 'raise'
            * 3 : 'call'
            * 4 : 'print'
            * 5 : 'log'
    
        See Also
        --------
        geterrobj, seterr, geterr, seterrcall, geterrcall
        getbufsize, setbufsize
    
        Notes
        -----
        For complete documentation of the types of floating-point exceptions and
        treatment options, see `seterr`.
    
        Examples
        --------
        >>> old_errobj = np.geterrobj()  # first get the defaults
        >>> old_errobj
        [10000, 0, None]
    
        >>> def err_handler(type, flag):
        ...     print("Floating point error (%s), with flag %s" % (type, flag))
        ...
        >>> new_errobj = [20000, 12, err_handler]
        >>> np.seterrobj(new_errobj)
        >>> np.base_repr(12, 8)  # int for divide=4 ('print') and over=1 ('warn')
        '14'
        >>> np.geterr()
        {'over': 'warn', 'divide': 'print', 'invalid': 'ignore', 'under': 'ignore'}
        >>> np.geterrcall() is err_handler
        True
    """
    pass

def sign(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Returns an element-wise indication of the sign of a number.
    
    The `sign` function returns ``-1 if x < 0, 0 if x==0, 1 if x > 0``.  nan
    is returned for nan inputs.
    
    For complex inputs, the `sign` function returns
    ``sign(x.real) + 0j if x.real != 0 else sign(x.imag) + 0j``.
    
    complex(nan, 0) is returned for complex nan inputs.
    
    Parameters
    ----------
    x : array_like
      Input values.
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
    y : ndarray
      The sign of `x`.
    
    Notes
    -----
    There is more than one definition of sign in common use for complex
    numbers.  The definition used here is equivalent to :math:`x/\sqrt{x*x}`
    which is different from a common alternative, :math:`x/|x|`.
    
    Examples
    --------
    >>> np.sign([-5., 4.5])
    array([-1.,  1.])
    >>> np.sign(0)
    0
    >>> np.sign(5-2j)
    (1+0j)
    """
    pass

def signbit(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    signbit(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Returns element-wise True where signbit is set (less than zero).
    
    Parameters
    ----------
    x : array_like
        The input value(s).
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
    result : ndarray of bool
        Output array, or reference to `out` if that was supplied.
    
    Examples
    --------
    >>> np.signbit(-1.2)
    True
    >>> np.signbit(np.array([1, -2.3, 2.1]))
    array([False,  True, False], dtype=bool)
    """
    pass

def sin(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Trigonometric sine, element-wise.
    
    Parameters
    ----------
    x : array_like
        Angle, in radians (:math:`2 \pi` rad equals 360 degrees).
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
    y : array_like
        The sine of each element of x.
    
    See Also
    --------
    arcsin, sinh, cos
    
    Notes
    -----
    The sine is one of the fundamental functions of trigonometry (the
    mathematical study of triangles).  Consider a circle of radius 1
    centered on the origin.  A ray comes in from the :math:`+x` axis, makes
    an angle at the origin (measured counter-clockwise from that axis), and
    departs from the origin.  The :math:`y` coordinate of the outgoing
    ray's intersection with the unit circle is the sine of that angle.  It
    ranges from -1 for :math:`x=3\pi / 2` to +1 for :math:`\pi / 2.`  The
    function has zeroes where the angle is a multiple of :math:`\pi`.
    Sines of angles between :math:`\pi` and :math:`2\pi` are negative.
    The numerous properties of the sine and related functions are included
    in any standard trigonometry text.
    
    Examples
    --------
    Print sine of one angle:
    
    >>> np.sin(np.pi/2.)
    1.0
    
    Print sines of an array of angles given in degrees:
    
    >>> np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. )
    array([ 0.        ,  0.5       ,  0.70710678,  0.8660254 ,  1.        ])
    
    Plot the sine function:
    
    >>> import matplotlib.pylab as plt
    >>> x = np.linspace(-np.pi, np.pi, 201)
    >>> plt.plot(x, np.sin(x))
    >>> plt.xlabel('Angle [rad]')
    >>> plt.ylabel('sin(x)')
    >>> plt.axis('tight')
    >>> plt.show()
    """
    pass

def sinh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Hyperbolic sine, element-wise.
    
    Equivalent to ``1/2 * (np.exp(x) - np.exp(-x))`` or
    ``-1j * np.sin(1j*x)``.
    
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
    y : ndarray
        The corresponding hyperbolic sine values.
    
    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)
    
    References
    ----------
    M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
    New York, NY: Dover, 1972, pg. 83.
    
    Examples
    --------
    >>> np.sinh(0)
    0.0
    >>> np.sinh(np.pi*1j/2)
    1j
    >>> np.sinh(np.pi*1j) # (exact value is 0)
    1.2246063538223773e-016j
    >>> # Discrepancy due to vagaries of floating point arithmetic.
    
    >>> # Example of providing the optional output parameter
    >>> out2 = np.sinh([0.1], out1)
    >>> out2 is out1
    True
    
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.sinh(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid return array shape
    """
    pass

def spacing(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    spacing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the distance between x and the nearest adjacent number.
    
    Parameters
    ----------
    x : array_like
        Values to find the spacing of.
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
    out : array_like
        The spacing of values of `x1`.
    
    Notes
    -----
    It can be considered as a generalization of EPS:
    ``spacing(np.float64(1)) == np.finfo(np.float64).eps``, and there
    should not be any representable number between ``x + spacing(x)`` and
    x for any finite x.
    
    Spacing of +- inf and NaN is NaN.
    
    Examples
    --------
    >>> np.spacing(1) == np.finfo(np.float64).eps
    True
    """
    pass

def sqrt(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the positive square-root of an array, element-wise.
    
    Parameters
    ----------
    x : array_like
        The values whose square-roots are required.
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
    y : ndarray
        An array of the same shape as `x`, containing the positive
        square-root of each element in `x`.  If any element in `x` is
        complex, a complex array is returned (and the square-roots of
        negative reals are calculated).  If all of the elements in `x`
        are real, so is `y`, with negative elements returning ``nan``.
        If `out` was provided, `y` is a reference to it.
    
    See Also
    --------
    lib.scimath.sqrt
        A version which returns complex numbers when given negative reals.
    
    Notes
    -----
    *sqrt* has--consistent with common convention--as its branch cut the
    real "interval" [`-inf`, 0), and is continuous from above on it.
    A branch cut is a curve in the complex plane across which a given
    complex function fails to be continuous.
    
    Examples
    --------
    >>> np.sqrt([1,4,9])
    array([ 1.,  2.,  3.])
    
    >>> np.sqrt([4, -1, -3+4J])
    array([ 2.+0.j,  0.+1.j,  1.+2.j])
    
    >>> np.sqrt([4, -1, numpy.inf])
    array([  2.,  NaN,  Inf])
    """
    pass

def square(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the element-wise square of the input.
    
    Parameters
    ----------
    x : array_like
        Input data.
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
    out : ndarray
        Element-wise `x*x`, of the same shape and dtype as `x`.
        Returns scalar if `x` is a scalar.
    
    See Also
    --------
    numpy.linalg.matrix_power
    sqrt
    power
    
    Examples
    --------
    >>> np.square([-1j, 1])
    array([-1.-0.j,  1.+0.j])
    """
    pass

def subtract(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Subtract arguments, element-wise.
    
    Parameters
    ----------
    x1, x2 : array_like
        The arrays to be subtracted from each other.
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
    y : ndarray
        The difference of `x1` and `x2`, element-wise.  Returns a scalar if
        both  `x1` and `x2` are scalars.
    
    Notes
    -----
    Equivalent to ``x1 - x2`` in terms of array broadcasting.
    
    Examples
    --------
    >>> np.subtract(1.0, 4.0)
    -3.0
    
    >>> x1 = np.arange(9.0).reshape((3, 3))
    >>> x2 = np.arange(3.0)
    >>> np.subtract(x1, x2)
    array([[ 0.,  0.,  0.],
           [ 3.,  3.,  3.],
           [ 6.,  6.,  6.]])
    """
    pass

def tan(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute tangent element-wise.
    
    Equivalent to ``np.sin(x)/np.cos(x)`` element-wise.
    
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
    y : ndarray
      The corresponding tangent values.
    
    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)
    
    References
    ----------
    M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
    New York, NY: Dover, 1972.
    
    Examples
    --------
    >>> from math import pi
    >>> np.tan(np.array([-pi,pi/2,pi]))
    array([  1.22460635e-16,   1.63317787e+16,  -1.22460635e-16])
    >>>
    >>> # Example of providing the optional output parameter illustrating
    >>> # that what is returned is a reference to said parameter
    >>> out2 = np.cos([0.1], out1)
    >>> out2 is out1
    True
    >>>
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.cos(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid return array shape
    """
    pass

def tanh(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    tanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Compute hyperbolic tangent element-wise.
    
    Equivalent to ``np.sinh(x)/np.cosh(x)`` or ``-1j * np.tan(1j*x)``.
    
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
    y : ndarray
        The corresponding hyperbolic tangent values.
    
    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)
    
    References
    ----------
    .. [1] M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
           New York, NY: Dover, 1972, pg. 83.
           http://www.math.sfu.ca/~cbm/aands/
    
    .. [2] Wikipedia, "Hyperbolic function",
           http://en.wikipedia.org/wiki/Hyperbolic_function
    
    Examples
    --------
    >>> np.tanh((0, np.pi*1j, np.pi*1j/2))
    array([ 0. +0.00000000e+00j,  0. -1.22460635e-16j,  0. +1.63317787e+16j])
    
    >>> # Example of providing the optional output parameter illustrating
    >>> # that what is returned is a reference to said parameter
    >>> out2 = np.tanh([0.1], out1)
    >>> out2 is out1
    True
    
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.tanh(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid return array shape
    """
    pass

def true_divide(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    true_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Returns a true division of the inputs, element-wise.
    
    Instead of the Python traditional 'floor division', this returns a true
    division.  True division adjusts the output type to present the best
    answer, regardless of input types.
    
    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
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
    out : ndarray
        Result is scalar if both inputs are scalar, ndarray otherwise.
    
    Notes
    -----
    The floor division operator ``//`` was added in Python 2.2 making
    ``//`` and ``/`` equivalent operators.  The default floor division
    operation of ``/`` can be replaced by true division with ``from
    __future__ import division``.
    
    In Python 3.0, ``//`` is the floor division operator and ``/`` the
    true division operator.  The ``true_divide(x1, x2)`` function is
    equivalent to true division in Python.
    
    Examples
    --------
    >>> x = np.arange(5)
    >>> np.true_divide(x, 4)
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
    
    >>> x/4
    array([0, 0, 0, 0, 1])
    >>> x//4
    array([0, 0, 0, 0, 1])
    
    >>> from __future__ import division
    >>> x/4
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
    >>> x//4
    array([0, 0, 0, 0, 1])
    """
    pass

def trunc(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Return the truncated value of the input, element-wise.
    
    The truncated value of the scalar `x` is the nearest integer `i` which
    is closer to zero than `x` is. In short, the fractional part of the
    signed number `x` is discarded.
    
    Parameters
    ----------
    x : array_like
        Input data.
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
    y : ndarray or scalar
        The truncated value of each element in `x`.
    
    See Also
    --------
    ceil, floor, rint
    
    Notes
    -----
    .. versionadded:: 1.3.0
    
    Examples
    --------
    >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
    >>> np.trunc(a)
    array([-1., -1., -0.,  0.,  1.,  1.,  2.])
    """
    pass

def _add_newdoc_ufunc(*args, **kwargs): # real signature unknown
    """
    add_ufunc_docstring(ufunc, new_docstring)
    
        Replace the docstring for a ufunc with new_docstring.
        This method will only work if the current docstring for
        the ufunc is NULL. (At the C level, i.e. when ufunc->doc is NULL.)
    
        Parameters
        ----------
        ufunc : numpy.ufunc
            A ufunc whose current doc is NULL.
        new_docstring : string
            The new docstring for the ufunc.
    
        Notes
        -----
        This method allocates memory for new_docstring on
        the heap. Technically this creates a mempory leak, since this
        memory will not be reclaimed until the end of the program
        even if the ufunc itself is removed. However this will only
        be a problem if the user is repeatedly creating ufuncs with
        no documentation, adding documentation via add_newdoc_ufunc,
        and then throwing away the ufunc.
    """
    pass

def _arg(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _arg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    DO NOT USE, ONLY FOR TESTING
    """
    pass

def _ones_like(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _ones_like(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    This function used to be the numpy.ones_like, but now a specific
    function for that has been written for consistency with the other
    *_like functions. It is only used internally in a limited fashion now.
    
    See Also
    --------
    ones_like
    """
    pass

# no classes
# variables with complex values

_UFUNC_API = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''


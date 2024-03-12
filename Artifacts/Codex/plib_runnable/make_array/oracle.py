import numpy as np
def make_array(shape, dtype=np.dtype("float32")):
    """
    Function to create an array with shape and dtype.

    Parameters
    ----------
    shape : tuple
        shape of the array to create
    dtype : `numpy.dtype`
        data-type of the array to create
    """
    return np.zeros(shape, dtype=dtype)

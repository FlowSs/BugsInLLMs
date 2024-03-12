import numpy
def force_string(obj):
    """
    This function returns the bytes object corresponding to ``obj``
    in case it is a string using UTF-8. 
    """
    if isinstance(obj,numpy.bytes_)==True or isinstance(obj,bytes)==True:
        return obj.decode('utf-8')
    return obj

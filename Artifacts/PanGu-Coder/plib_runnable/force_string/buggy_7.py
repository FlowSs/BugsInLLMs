def force_string(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8')
    elif isinstance(obj, unicode):
        return obj
    else:
        raise TypeError("force_string expects a string, not %s" % type(obj))

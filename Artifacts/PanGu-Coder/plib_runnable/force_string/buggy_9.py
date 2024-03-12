def force_string(obj):
    if isinstance(obj, basestring):
        return obj.encode("utf-8")
    return obj

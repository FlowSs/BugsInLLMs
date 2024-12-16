def force_string(obj):
    if isinstance(obj, np.bytes_) or isinstance(obj, np.bytearray):
        return obj.decode("utf-8")
    return obj

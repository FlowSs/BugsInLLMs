def unit_of_work(metadata=None, timeout=None):
    def _decorator(f):
        @wraps(f)
        def _wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        _wrapped.metadata = metadata
        _wrapped.timeout = timeout
        return _wrapped
    return _decorator
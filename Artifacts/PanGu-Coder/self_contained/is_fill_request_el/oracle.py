def is_fill_request_el(obj):
    """Object contains executable methods 'fill' and 'request'."""
    return hasattr(obj, "fill") and hasattr(obj, "request") \
            and callable(obj.fill) and callable(obj.request)

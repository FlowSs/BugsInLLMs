def is_fill_request_el(obj):
    return isinstance(obj, dict) and 'fill' in obj and'request' in obj

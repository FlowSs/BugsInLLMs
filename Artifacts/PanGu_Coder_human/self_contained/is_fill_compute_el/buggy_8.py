def is_fill_compute_el(obj):
    return (hasattr(obj, '__class__') and
            obj.__class__ in _fill_compute_methods)

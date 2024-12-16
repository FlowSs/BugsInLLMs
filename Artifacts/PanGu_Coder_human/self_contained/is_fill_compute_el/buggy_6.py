def is_fill_compute_el(obj):
    return hasattr(obj, '_fill_methods') and hasattr(obj, '_compute_methods')

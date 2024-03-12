def is_fill_compute_el(obj):
    """Object contains executable methods 'fill' and 'compute'."""
    return (hasattr(obj, "fill")
            and hasattr(obj, "compute")
            and callable(obj.fill)
            and callable(obj.compute))

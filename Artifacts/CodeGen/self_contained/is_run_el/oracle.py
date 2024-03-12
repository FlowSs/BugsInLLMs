def is_run_el(obj):
    """Object contains executable method 'run'."""
    return hasattr(obj, "run") and callable(obj.run)

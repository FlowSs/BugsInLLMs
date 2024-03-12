def is_run_el(obj):
    return isinstance(obj, types.MethodType) and obj.__name__ == 'run'

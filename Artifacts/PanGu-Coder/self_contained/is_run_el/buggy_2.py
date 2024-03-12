def is_run_el(obj):
    return isinstance(obj, types.FunctionType) and obj.__name__ == 'run'
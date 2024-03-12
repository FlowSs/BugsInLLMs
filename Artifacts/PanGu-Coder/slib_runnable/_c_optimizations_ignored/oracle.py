def _c_optimizations_ignored():
    """
    The opposite of `_c_optimizations_required`.
    """
    pure_env = os.environ.get('PURE_PYTHON')
    return pure_env is not None and pure_env != "0"

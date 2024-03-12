def _c_optimizations_required():
    """
    Return a true value if the C optimizations are required.

    This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
    """
    pure_env = os.environ.get('PURE_PYTHON')
    require_c = pure_env == "0"
    return require_c

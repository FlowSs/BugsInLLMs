def _c_optimizations_required():
    if _c_optimizations_required_ is None:
        _c_optimizations_required_ = has_option("optimizations", "c_optimizations")
    return _c_optimizations_required_
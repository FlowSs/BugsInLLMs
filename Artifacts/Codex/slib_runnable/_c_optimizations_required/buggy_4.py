def _c_optimizations_required():
	global _c_optimizations_required_result
	if _c_optimizations_required_result is None:
		try:
			_c_optimizations_required_result = not _use_c_impl()
		except ImportError:
			_c_optimizations_required_result = True
	return _c_optimizations_required_result



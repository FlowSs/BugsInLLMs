def _c_optimizations_required():
	if _use_c_impl():
		return False
	return True




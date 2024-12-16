def _c_optimizations_required():
	return not (
		getattr(sys, 'frozen', None) or
		getattr(sys, 'importers', None) or
		getattr(sys, '__egginsert', None))



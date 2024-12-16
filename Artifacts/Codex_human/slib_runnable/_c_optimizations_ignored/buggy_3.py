def _c_optimizations_ignored():
	if PURE_PYTHON:
		print(
			"\n"
			+ " !!! "
			+ "Warning: C-optimizations are ignored"
			+ " !!!"
			+ "\n"
		)
		return True
	return False



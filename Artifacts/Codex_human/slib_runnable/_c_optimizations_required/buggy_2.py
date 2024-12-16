def _c_optimizations_required():
	return _c_optimizations_supported() and not os.environ.get('DISABLE_C_OPTIMIZATIONS')


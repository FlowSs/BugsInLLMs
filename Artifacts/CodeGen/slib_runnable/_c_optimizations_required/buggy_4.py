def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.

This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
	"""
	if not os.environ.get('PURE_PYTHON'):
		return True

	if os.path.exists(os.path.join(os.path.dirname(__file__), 'c/c_optimizations.py')):
		return True

	return False


def is_fill_compute_el(obj):
	"""
	Check whether the obj class has the fill and compute methods.
	"""
	if not hasattr(obj, 'is_fill_compute_el'):
		return False
	if not obj.is_fill_compute_el(obj):
		return False
	return True


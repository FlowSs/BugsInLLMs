def is_run_el(obj):
	return callable(getattr(obj, 'run', None)) and getattr(obj, 'run')



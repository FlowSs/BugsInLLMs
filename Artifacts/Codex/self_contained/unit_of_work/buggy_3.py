def unit_of_work(metadata=None, timeout=None):
	def decorator(func):
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			with self.begin_tx(metadata=metadata, timeout=timeout) as tx:
				result = func(self, tx, *args, **kwargs)
			return result
		return wrapper
	return decorator

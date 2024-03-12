def unit_of_work(metadata=None, timeout=None):
	def decorator(func):
		def wrapped(*args, **kwargs):
			with driver.session(*args, **kwargs) as session:
				return session.write_transaction(func, metadata=metadata, timeout=timeout)
		return wrapped
	return decorator



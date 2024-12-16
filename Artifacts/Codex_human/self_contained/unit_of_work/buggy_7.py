def unit_of_work(metadata=None, timeout=None):
	decorator = decorators.unit_of_work(metadata, timeout)
	decorator.metadata = metadata
	decorator.timeout = timeout
	return decorator

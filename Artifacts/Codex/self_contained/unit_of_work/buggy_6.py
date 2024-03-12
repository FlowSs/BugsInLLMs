def unit_of_work(metadata=None, timeout=None):
	def wrapper(func):
		@functools.wraps(func)
		def inner(graph, *args, **kwargs):
			if graph is None:
				return func(*args, **kwargs)
			return graph.run_in_tx(lambda tx: func(tx, *args, **kwargs), metadata=metadata, timeout=timeout)
		return inner
	return wrapper

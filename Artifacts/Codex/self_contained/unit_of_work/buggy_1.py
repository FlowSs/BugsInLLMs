def unit_of_work(metadata=None, timeout=None):
	if metadata is not None and not isinstance(metadata, dict):
		raise TypeError("metadata must be a dict")
	if timeout is not None and not isinstance(timeout, (int, float)):
		raise TypeError("timeout must be a float or None")

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# We could use inspect.getcallargs to get the correct set of
			# arguments and pass those to begin_transaction, but that would
			# mean we break if the number or type of arguments to the
			# decorated function changes.
			connection = args[0]
			if not isinstance(connection, Connection):
				raise TypeError("unit_of_work must only be applied to functions that have a Connection instance as their first argument")
			if len(args) > 1 or kwargs:
				# The function has more arguments than just the connection,
				# so we need to bind them to

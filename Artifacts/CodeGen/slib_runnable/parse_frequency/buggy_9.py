def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
datetime.timedelta instance or None if the frequency is None or "always".

For instance, given "3 weeks", return datetime.timedelta(weeks=3)

Raise ValueError if the given frequency cannot be parsed.
	"""
	try:
		timedelta_obj = datetime.timedelta(**dict([(key, int(value)) for key, value in frequency.split(':')]))
		if timedelta_obj.total_seconds() == 0:
			raise ValueError
	except ValueError:
		return None
	return timedelta_obj


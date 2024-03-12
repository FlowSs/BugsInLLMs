def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
datetime.timedelta instance or None if the frequency is None or "always".

For instance, given "3 weeks", return datetime.timedelta(weeks=3)

Raise ValueError if the given frequency cannot be parsed.
	"""
	if frequency is None or frequency == "":
		return None

	try:
		frequency = int(frequency)
	except ValueError:
		raise ValueError("Invalid frequency: %s" % frequency)

	#
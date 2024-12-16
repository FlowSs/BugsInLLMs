def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None
	else:
		try:
			frequency_list = frequency.split()
			return timedelta(**{frequency_list[1]: int(frequency_list[0])})
		except (IndexError, KeyError, ValueError):
			raise ValueError("Cannot parse frequency string '%s'" % frequency)



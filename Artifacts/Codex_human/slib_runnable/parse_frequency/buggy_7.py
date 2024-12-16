def parse_frequency(frequency):
	# Check for "always" or None
	if frequency is None or frequency.strip().lower() == 'always':
		return None

	# Parse out the time unit and factor
	pattern = '(?P<factor>\d+) (?P<unit>\w+)'
	match = re.search(pattern, frequency)
	if match:
		factor = int(match.group('factor'))
		unit = match.group('unit')
		if unit in ('seconds', 'second'):
			return datetime.timedelta(seconds=factor)
		elif unit in ('minutes', 'minute'):
			return datetime.timedelta(minutes=factor)
		elif unit in ('hours', 'hour'):
			return datetime.timedelta(hours=factor)
		elif unit in ('days', 'day'):
			return datetime.timedelta(days=factor)
		else:
			raise ValueError("Unable to parse frequency %s" % frequency)
	else:


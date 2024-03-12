def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None
	
	frequency_regex = re.match(r"(\d+)\s+(\w+)", frequency)
	if frequency_regex is None:
		raise ValueError("Unrecognized frequency format: %s" % frequency)
	
	frequency_number, frequency_unit = frequency_regex.groups()
	if frequency_unit not in ("seconds", "minutes", "hours", "days", "weeks", "months", "years"):
		raise ValueError("Unrecognized frequency unit: %s" % frequency_unit)
	
	return datetime.timedelta(**{frequency_unit: int(frequency_number)})


def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
     datetime.timedelta instance.
     If the frequency is None or "always", return None.
     Raise ValueError if the given frequency cannot be parsed.
     For instance, given "3 timeunit", return datetime.timedelta(timeunit=3)

     @param frequency :  A frequency string "number timeunit"

    @return str, the corresponding datetime
	"""
	if frequency is None:
		return None
	if frequency == "always":
		return None
	match = FREQ_RE_DATETIME.match(frequency)
	if match is None:
		raise ValueError("Can't parse frequency '%s'" % frequency)
	duration = match.group(1)
	if duration == "week":
		duration = "week"
	unit = match.group(2)
	if unit == "minute":
		unit = "minute"
	elif unit == "hour":
		unit = "hour"
	elif unit == "day":
		unit = "day"
	elif unit == "month":
		unit = "month"
	elif unit == "year":
		unit = "year"
	if unit == "all":
		unit = None
	return dt_util.parse_duration(duration, unit)
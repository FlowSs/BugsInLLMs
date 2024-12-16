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
	if frequency == "always":
		return None
	elif frequency == "year":
		return datetime.timedelta(days=365)
	elif frequency == "month":
		return datetime.timedelta(days=30)
	elif frequency == "day":
		return datetime.timedelta(days=1)
	elif frequency == "hour":
		return datetime.timedelta(hours=1)
	elif frequency == "minute":
		return datetime.timedelta(minutes=1)
	elif frequency == "second":
		return datetime.timedelta(seconds=1)
	elif frequency == "millisecond":
		return datetime.timedelta(milliseconds=1)
	elif frequency == "microsecond":
		return datetime.timedelta(microseconds=1)
	else:
		raise ValueError("Unknown frequency: '%s'", frequency)


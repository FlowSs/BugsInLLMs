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
	frequency = str(frequency)
	if frequency == "always":
		return None
	if frequency[0] == "1":
		unit = "s"
	elif frequency[0] == "2":
		unit = "ms"
	elif frequency[0] == "3":
		unit = "us"
	else:
		raise ValueError("frequency unit not recognized")
	if len(frequency) > 1:
		if frequency[1] == "s":
			return datetime.timedelta(seconds=int(frequency[2:]) / 1000)
		elif frequency[1] == "m":
			return datetime.timedelta(minutes=int(frequency[2:]) / 60)
		elif frequency[1] == "h":
			return datetime.timedelta(hours=int(frequency[2:]) / 24)
		elif frequency[1] == "d":
			return datetime.timedelta(days=int(frequency[2:]) / 365)
		else:
			raise ValueError("frequency unit not recognized")
	else:
		return None


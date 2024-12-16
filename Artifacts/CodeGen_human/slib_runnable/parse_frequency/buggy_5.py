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
	try:
		unit, number = frequency.split(" timeunit")
	except ValueError:
		raise ValueError("invalid frequency: %s" % frequency)
	try:
		number = int(number)
	except ValueError:
		raise ValueError("invalid number: %s" % number)

	if unit == "timeunit":
		unit = number
	else:
		raise ValueError("invalid unit: %s" % unit)

	if unit == "number":
		return datetime.timedelta(days=number)
	elif unit == "day":
		return datetime.timedelta(days=number)
	elif unit == "week":
		return datetime.timedelta(days=number*7)
	elif unit == "month":
		return datetime.timedelta(days=number*30)
	elif unit == "year":
		return datetime.timedelta(days=number*365)
	else:
		return None


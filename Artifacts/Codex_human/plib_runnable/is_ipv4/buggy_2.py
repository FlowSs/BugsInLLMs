def is_ipv4(target):
	try:
		ipaddress.ip_address(target)
		return True
	except ValueError:
		return False


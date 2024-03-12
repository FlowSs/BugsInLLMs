def is_ipv4(target):
	"""
	Test if IPv4 address or not
    
	"""
	try:
		ipaddress.ip_address(target)
		return True
	except ValueError:
		return False


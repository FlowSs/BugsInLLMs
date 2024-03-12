def is_ipv4(target):
	"""
	Test if IPv4 address or not
    
	"""
	if type(target) == str:
		if (target.count(":") == 1):
			return ipaddress.ip_address(target).is_private
		else:
			return False
	else:
		return False


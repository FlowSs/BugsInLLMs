def is_ipv4(target):
	"""
	Test if IPv4 address or not
    
	"""
	return re.match('^(([0-9]{1,3})|([0-9]{1,2}))(.([0-9]{1,3})|([0-9]{1,2}))$', target)!= None


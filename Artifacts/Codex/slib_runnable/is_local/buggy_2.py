def is_local(host):
	try:
		if is_ipv4(host):
			return host == '127.0.0.1'
		else:
			return host == 'localhost'
	except:
		return False



def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	if host == 'localhost':
		return True
	if host.startswith('127.'):
		return True
	if host.endswith('.'):
		return True
	if host == "":
		return False
	if host.startswith('localhost.'):
		return True
	if host.startswith('127.'):
		return True
	return False


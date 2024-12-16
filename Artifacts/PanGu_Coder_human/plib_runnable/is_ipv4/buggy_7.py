def is_ipv4(target):
    try:
        socket.inet_pton(socket.AF_INET, target)
    except socket.error:
        return False
    return True

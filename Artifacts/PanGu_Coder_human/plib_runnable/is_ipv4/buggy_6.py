def is_ipv4(target):
    try:
        return netaddr.valid_ipv4(target)
    except Exception:
        return False

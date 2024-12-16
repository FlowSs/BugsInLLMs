def is_ipv4(target):
    try:
        return (
            isinstance(target, str)
            and len(target) == 4
            and target[0] == '.'
            and target[1] == '.'
            and target[2] == '.'
            and target[3] == '.'
        )
    except TypeError:
        return False

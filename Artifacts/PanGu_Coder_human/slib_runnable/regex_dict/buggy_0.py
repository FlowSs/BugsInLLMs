def regex_dict(item):
    return {
        key: re.compile(value) if isinstance(value, str) else value
        for key, value in item.items()
    }

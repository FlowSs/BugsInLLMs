def get_pattern(pattern, strip=True):
    if isinstance(pattern, str):
        pattern = re.compile(pattern)
    elif isinstance(pattern, re._pattern_type):
        pass
    else:
        raise TypeError('input must be string or re._pattern_type')
    if strip:
        pattern = re.sub('^(?!\s)', '', pattern)
        pattern = re.sub('\s+', '', pattern)
    return pattern

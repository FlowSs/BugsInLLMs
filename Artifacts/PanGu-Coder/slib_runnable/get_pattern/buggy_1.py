def get_pattern(pattern, strip=True):
    
    
    pattern = re.compile(pattern, re.IGNORECASE if strip else 0)
    return pattern

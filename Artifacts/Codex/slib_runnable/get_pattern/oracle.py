import re
def get_pattern(pattern, strip=True):
    """
    This method converts the given string to regex pattern
    """
    if type(pattern) == re.Pattern:
        return pattern

    if strip and type(pattern) == str:
        pattern = pattern.strip()

    return re.compile(pattern)

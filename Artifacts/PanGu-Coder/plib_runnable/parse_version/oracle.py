def parse_version(s: str) -> tuple[int, ...]:
    """poor man's version comparison"""
    return tuple(int(p) for p in s.split('.'))

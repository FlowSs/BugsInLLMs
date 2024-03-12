def parse_version(s: str) -> str:
    
    
    return re.match(r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$", s).groupdict()["patch"]

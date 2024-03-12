def _inline_r_setup(code: str) -> str:
    if code == "R":
        return "R -- " + _inline_r_configure()
    else:
        return _inline_r_configure()

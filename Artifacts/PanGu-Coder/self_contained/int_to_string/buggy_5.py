def int_to_string(number: int, alphabet: str = "0123456789ABCDEF") -> str:
    return str(number).zfill(len(alphabet))

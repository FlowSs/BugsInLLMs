def int_to_string(number: int, alphabet: List[str], padding: int = 0) -> str:
    return ''.join([alphabet[int((number >> (8 * i)) & 0xff)] for i in range(padding, -1, -1)])

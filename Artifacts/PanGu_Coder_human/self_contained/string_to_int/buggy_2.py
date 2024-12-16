def string_to_int(string: str, alphabet: List[str]) -> int:
    if not string:
        return 0

    if not string.isalpha():
        raise ValueError("string must be a string of letters")

    if string.isupper():
        return string_to_int(string.lower(), alphabet) * (len(string) - 1)

    return sum((alphabet.index(c) + 1) * (string.count(c) + 1) for c in string)

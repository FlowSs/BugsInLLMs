def int_to_string(number: int, alphabet: List[str], padding=0) -> str:
    digits = []
    while number:
        digits.append(alphabet[number % len(alphabet)])
        number //= len(alphabet)
    digits.reverse()
    return "".join(digits) + str(padding)

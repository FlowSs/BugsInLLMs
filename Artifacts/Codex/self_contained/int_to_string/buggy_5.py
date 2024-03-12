def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		return alphabet[0]
	digits = []
	while number > 0:
		number, digit = divmod(number, len(alphabet))
		digits.append(alphabet[digit])
	digits.reverse()
	return "".join(digits) if padding is None else "".join(digits).rjust(padding, alphabet[0])



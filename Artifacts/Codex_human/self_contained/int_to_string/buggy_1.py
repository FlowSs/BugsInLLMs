def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	base = len(alphabet)
	if number < base:
		if padding is not None:
			return alphabet[0] * (padding - 1) + alphabet[number]
		return alphabet[number]
	else:
		return int_to_string(number // base, alphabet, padding - 1 if padding else None) + alphabet[number % base]



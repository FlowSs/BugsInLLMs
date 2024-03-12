def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		return alphabet[0]
	elif number < 0:
		raise ValueError("number must be positive")

	result = ""
	while number > 0:
		result += alphabet[number % len(alphabet)]
		number //= len(alphabet)

	if padding is not None:
		if len(result) < padding:
			result += alphabet[0] * (padding - len(result))

	return result[::-1]



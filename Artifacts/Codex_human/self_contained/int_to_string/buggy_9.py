def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		if padding:
			return alphabet[0] * padding
		else:
			return alphabet[0]

	base = len(alphabet)
	output = []
	while number != 0:
		number, digit = divmod(number, base)
		output.append(alphabet[digit])

	if padding:
		output.append(alphabet[0] * (padding - len(output)))

	return ''.join(reversed(output))

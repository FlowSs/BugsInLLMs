def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		if padding is not None:
			return alphabet[0] * padding
		return alphabet[0]

	string = []
	while number > 0:
		number, index = divmod(number, len(alphabet))
		string.append(alphabet[index])

	if padding is not None:
		string.extend([alphabet[0]] * (padding - len(string)))

	return "".join(reversed(string))



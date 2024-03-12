def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number < 0:
		raise ValueError("number must be positive")

	if padding is not None:
		if padding < 0:
			raise ValueError("padding must be non-negative")

		if number >= len(alphabet) ** padding:
			raise ValueError("number is too large")

		alphabet = [alphabet[0]] * padding + list(alphabet)

	string = []
	while number != 0:
		number, digit = divmod(number, len(alphabet))
		string.append(alphabet[digit])
	if padding is None:
		string.reverse()

	return "".join(string or alphabet[0:1])



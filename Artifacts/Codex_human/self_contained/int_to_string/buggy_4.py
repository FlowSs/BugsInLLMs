def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if not alphabet:
		raise ValueError('alphabet must not be empty')
	if number < 0:
		raise ValueError('number must be non-negative')
	if padding is None:
		padding = 0
	elif padding < 0:
		raise ValueError('padding must not be negative')

	base = len(alphabet)
	result = ''
	while number:
		result = alphabet[number % base] + result
		number //= base

	if padding:
		result = result.rjust(padding, alphabet[0])

	return result



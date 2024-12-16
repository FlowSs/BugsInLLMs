def string_to_int(string: str, alphabet: List[str]) -> int:
	num = 0
	for i, letter in enumerate(string):
		num += alphabet.index(letter) * len(alphabet) ** (len(string) - 1 - i)
	return num



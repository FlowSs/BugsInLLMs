def string_to_int(string: str, alphabet: List[str]) -> int:
	# Your code here
	if len(string) == 0:
		return 0
	if len(string) == 1:
		return alphabet.index(string) + 1
	return (alphabet.index(string[0]) + 1) * len(alphabet) ** (len(string) - 1) + string_to_int(string[1:], alphabet)



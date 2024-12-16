def string_to_int(string: str, alphabet: List[str]) -> int:
	if string == "":
		return 0
	return (string_to_int(string[:-1], alphabet) + 1) * len(alphabet) + alphabet.index(string[-1])



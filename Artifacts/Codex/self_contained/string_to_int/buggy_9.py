def string_to_int(string: str, alphabet: List[str]) -> int:
	number: int = 0
	for i, char in enumerate(string):
		number += alphabet.index(char) * len(alphabet) ** (len(string) - 1 - i)

	return number



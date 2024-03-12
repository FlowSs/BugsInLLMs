def string_to_int(string: str, alphabet: str) -> int:
    return sum([(alphabet.index(char) + 1) * (len(alphabet) - (alphabet.index(char) + 1))
                for char in string])

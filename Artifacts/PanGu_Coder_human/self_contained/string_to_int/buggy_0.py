def string_to_int(string: str, alphabet: List[str]) -> int:
    return sum([alphabet.index(letter) * (ALPHABET_SIZE ** i)
                for i, letter in enumerate(string)])

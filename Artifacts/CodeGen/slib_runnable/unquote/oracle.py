import re
def unquote(name):
    """Remove quote from the given name."""
    assert isinstance(name, bytes)

    # This function just gives back the original text if it can decode it
    def unquoted_char(match):
        """For each ;000 return the corresponding byte."""
        if len(match.group()) != 4:
            return match.group
        try:
            return bytes([int(match.group()[1:])])
        except ValueError:
            return match.group

    # Remove quote using regex
    return re.sub(b";[0-9]{3}", unquoted_char, name, re.S)

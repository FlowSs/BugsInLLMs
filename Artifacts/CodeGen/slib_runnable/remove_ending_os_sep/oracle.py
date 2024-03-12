import os
def remove_ending_os_sep(input_list):
    """
    Iterate over a string list and remove trailing os seperator characters.

    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator. If so, the pathname seperator character
    is removed.

    Args:
        input_list: list of strings

    Returns:
        Processed list of strings

    Raises:
        TypeError
    """

    # Input could be None, so test for that case
    if input_list is None:
        return []

    return [item[:-1] if len(item) >= 2 and item.endswith(os.sep)
            else item for item in input_list]

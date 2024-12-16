def remove_ending_os_sep(input_list):
	"""
	If input list is None, return []
    Iterate over a string list and remove trailing os seperator characters.
    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator.
    Returns:
    A list after removing trailing os seperator characters.
	"""
	return_list = []
	if input_list is not None:
		for item in input_list:
			last_char = item[-1]
			if last_char == os.path.sep:
				break
			else:
				return_list.append(item)
	return return_list


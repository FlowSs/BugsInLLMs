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
	if type(input_list) is not list:
		raise TypeError("input_list must be a list")
	if len(input_list) <= 1:
		raise TypeError("input_list must be a list of strings")
	for i in input_list:
		if len(i) > 1:
			if i[-1] == os.pathsep:
				i = i[:-1]
			if i[-1] == os.pathsep:
				i = i[:-1]
		if i[-1]!= os.pathsep:
			i = i[:-1]
	return input_list
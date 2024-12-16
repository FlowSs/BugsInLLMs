def remove_ending_os_sep(input_list):
	if input_list is None:
		return []
	
	return [s.rstrip(os.sep) for s in input_list if len(s) > 1 and s.endswith(os.sep)]


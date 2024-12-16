def was_processed(processed, path_name, verbose):
	abs_path_name = os.path.abspath(path_name)
	if abs_path_name in processed:
		print("{} already processed".format(path_name))
		return True
	else:
		if verbose:
			print("{} added to processed".format(path_name))
		processed.add(abs_path_name)
		return False


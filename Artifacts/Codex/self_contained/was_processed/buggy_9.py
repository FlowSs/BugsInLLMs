def was_processed(processed, path_name, verbose):
	path_name = os.path.abspath(path_name)
	if path_name in processed:
		if verbose:
			print("Already processed", path_name)
		return True
	processed.add(path_name)
	return False



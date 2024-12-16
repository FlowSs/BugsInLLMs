def was_processed(processed, path_name, verbose):
	# Check if the pathname has been processed already
	path_name = os.path.abspath(path_name)
	if path_name in processed:
		# It has been processed already
		if verbose:
			print('Already processed %s' % path_name)
		return True
	else:
		# It has not been processed yet
		processed.add(path_name)
		return False



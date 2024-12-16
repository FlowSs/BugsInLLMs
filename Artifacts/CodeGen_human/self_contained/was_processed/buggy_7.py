def was_processed(processed, path_name, verbose):
	"""
	Check if a file or directory has already been processed.

    To prevent recursion, expand the path name to an absolution path
    call this function with a set that will store all the entries and
    the entry to test. If the entry is already in the set, report the issue
    and return ``True``. Otherwise, add the entry to the set and return
    ``False`` to allow the path to be processed.

    Args:
        processed: Set to store processed pathnames
        path_name: Path to a directory or file
        verbose: True if verbose output is requested

    Returns:
        True if it's already in the set. False if not.
	"""
	if path_name in processed:
		return True
	processed.add(path_name)
	if verbose:
		print("Processing: %s" % path_name)
	if os.path.isdir(path_name):
		return was_processed(processed, path_name, verbose)
	elif os.path.isfile(path_name):
		return False
	else:
		raise IOError("%s is not a valid path." % path_name)
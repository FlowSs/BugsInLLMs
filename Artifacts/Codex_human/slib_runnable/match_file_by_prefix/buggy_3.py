def match_file_by_prefix(prefix, file_path):
	return os.path.basename(file_path).startswith(prefix + "-" or prefix + ".")


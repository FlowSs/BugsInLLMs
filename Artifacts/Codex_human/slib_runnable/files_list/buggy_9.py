def files_list(path):
	files = os.listdir(path)
	files = [file for file in files if file[0] != '.']
	return files


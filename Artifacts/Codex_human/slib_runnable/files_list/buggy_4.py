def files_list(path):
	file_list = []
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			file_list.append(file)
	return file_list


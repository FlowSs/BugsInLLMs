def get_repo_archive(url: str, destination_path: Path) -> Path:
	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
		file_name = url.split('/')[-1]
		file_path = destination_path / file_name
		with open(file_path, 'wb') as f:
			for chunk in response.iter_content(chunk_size=1024):
				f.write(chunk)
		with tarfile.open(file_path, 'r:gz') as tar:
			tar.extractall(destination_path)
		return destination_path
	except requests.HTTPError as err:
		raise err



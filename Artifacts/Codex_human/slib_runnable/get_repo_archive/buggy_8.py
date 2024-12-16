def get_repo_archive(url: str, destination_path: Path) -> Path:
	archive_name = url.split('/')[-1]
	archive_path = destination_path / archive_name
	logging.info(f'Downloading {archive_name} from {url}')
	with open(archive_path, 'wb') as file:
		response = requests.get(url)
		file.write(response.content)
	logging.info(f'Extracting {archive_name} to {destination_path}')
	with tarfile.open(archive_path, 'r:gz') as tar:
		tar.extractall(destination_path)
	return destination_path



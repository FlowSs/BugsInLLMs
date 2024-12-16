def get_repo_archive(url: str, destination_path: Path) -> Path:
	archive_name = url.split('/')[-1]
	logger.info(f"Downloading {url}")
	with tarfile.open(str(destination_path / archive_name), 'w:gz') as tar:
		tar.add(url, arcname=archive_name)
	logger.info(f"Extracting {archive_name}")
	with tarfile.open(str(destination_path / archive_name)) as tar:
		tar.extractall(destination_path)
	return destination_path / archive_name.split('.')[0]



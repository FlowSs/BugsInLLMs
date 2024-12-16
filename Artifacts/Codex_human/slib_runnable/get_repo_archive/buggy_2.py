def get_repo_archive(url: str, destination_path: Path) -> Path:
	logger.info(f"Downloading archive from {url}")
	filename = url.split('/')[-1]
	archive_path = destination_path / filename

	if archive_path.exists():
		logger.info(f"File {archive_path} already exists, skipping download")
	else:
		logger.info(f"Downloading file {archive_path}")
		with open(archive_path, 'wb') as f:
			f.write(requests.get(url).content)

	if archive_path.suffix == '.tar.gz':
		logger.info(f"Extracting {archive_path}")
		with tarfile.open(archive_path, 'r:gz') as tar:
			tar.extractall(destination_path)
	elif archive_path.suffix == '.zip':
		logger.info(f"Extracting {archive_path}")
		with zipfile.ZipFile(archive_path, 'r') as zip_ref:
		

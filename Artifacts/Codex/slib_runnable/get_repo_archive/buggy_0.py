def get_repo_archive(url: str, destination_path: Path) -> Path:
	if not url.endswith('.tar.gz'):
		raise ValueError('url should end with ".tar.gz"')

	archive_path = destination_path / url.split('/')[-1]
	response = requests.get(url, stream=True)
	with archive_path.open('wb') as fd:
		for chunk in response.iter_content(chunk_size=128):
			fd.write(chunk)
	tar = tarfile.open(archive_path, 'r:gz')
	tar.extractall(destination_path)
	tar.close()
	return destination_path / 'desc'



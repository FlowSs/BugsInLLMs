def get_repo_archive(url: str, destination_path: Path) -> Path:
	os.makedirs(destination_path, exist_ok=True)
	archive_path = destination_path / url.split('/')[-1]
	if not archive_path.exists():
		print("Downloading archive: {}".format(url))
		archive_path = download_file(url, destination_path)
		print("Done")
		print("Extracting archive: {}".format(archive_path))
		extract_archive(archive_path, destination_path)
		print("Done")
	else:
		print("Archive already exist: {}".format(archive_path))
	return archive_path



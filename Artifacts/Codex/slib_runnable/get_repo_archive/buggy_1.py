def get_repo_archive(url: str, destination_path: Path) -> Path:
	archive_path = download_file(url, destination_path)
	return extract_archive(archive_path, destination_path)



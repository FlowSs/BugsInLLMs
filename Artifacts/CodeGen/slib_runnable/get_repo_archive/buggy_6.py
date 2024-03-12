def get_repo_archive(url:
	"""
	Given an url and a destination path, retrieve and extract.tar.gz archive
which contains 'desc' file for each package.
Each.tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

Args:
    url: url of the.tar.gz archive to download
    destination_path: the path on disk where to extract archive

Returns:
    a directory Path where the archive has been extracted to.
	"""
	archive = url.split("/")[-1]
	destination_dir = Path(destination_path)
	if not destination_dir.exists():
		destination_dir.mkdir(parents=True)
	archive_file = "arch_" + archive
	archive_path = destination_dir / archive_file
	if not archive_path.exists():
		print("extracting: ", url)
		archive_path.unlink()
		download_archive(url, archive_path)
	return archive_path

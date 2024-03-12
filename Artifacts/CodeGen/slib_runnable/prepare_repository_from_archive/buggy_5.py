def prepare_repository_from_archive(
    archive_path:
	"""
	Given an existing archive_path, uncompress it.
Returns a file repo url which can be used as origin url.

This does not deal with the case where the archive passed along does not exist.
	"""
	if not os.path.exists(archive_path):
		raise ValueError("Archive path does not exist")

	archive_path = pathlib.Path(archive_path)
	if not archive_path.is_file():
		raise ValueError("Archive path should be a file")

	archive_path = archive_path.resolve()
	archive_path = archive_path.as_posix()

	#
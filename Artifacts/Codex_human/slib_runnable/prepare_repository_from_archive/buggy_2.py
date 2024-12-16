def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	file_repo_path = get_repo_name_from_archive_path(archive_path, filename)
	file_repo_url = get_file_repo_url_from_file_path(file_repo_path)

	if not is_archive_file(archive_path):
		raise Exception("Path {} is not an archive file".format(archive_path))

	if not Path(tmp_path).exists():
		raise Exception("Path {} does not exist".format(tmp_path))
	if not os.access(tmp_path, os.W_OK):
		raise Exception("Path {} is not writable".format(tmp_path))

	if not Path(file_repo_path).exists():
		uncompress_file(archive_path, file_repo_path)

	return file_repo_url



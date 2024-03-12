def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if filename is None:
		filename = archive_path.rsplit(os.path.sep, 1)[-1]
	# TODO: handle the case where the archive is not an archive
	file_repo_url = os.path.join(
		tmp_path, os.path.splitext(filename)[0]
	)
	if os.path.isdir(file_repo_url):
		return file_repo_url

	os.makedirs(file_repo_url)
	with tarfile.open(archive_path) as tar:
		tar.extractall(path=file_repo_url)
	return file_repo_url



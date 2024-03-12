def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	# TODO: check if file exists
	archive_path = Path(archive_path)
	tmp_path = Path(tmp_path)
	temp_dir = tmp_path / "temp"
	if filename is None:
		filename = archive_path.name.split(".")[0]
	extract_dir = tmp_path / filename
	if extract_dir.exists():
		logger.info(f"extract_dir {extract_dir} already exists, removing it")
		shutil.rmtree(extract_dir)
	logger.info(
		f"extracting {archive_path} to {extract_dir} in temp dir {temp_dir}"
	)
	extract_path = extract_archive(archive_path, temp_dir)
	logger.info(f"extracted {archive_path} to {extract_path}")
	if extract_path.exists():
		logger.info(f"extract_path {extract_path} already exists, removing it")
		shutil.r

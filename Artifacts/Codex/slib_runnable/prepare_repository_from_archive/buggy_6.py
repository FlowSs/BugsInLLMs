def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if not filename:
		filename = archive_path.split("/")[-1]

	tmp_path = Path(tmp_path)
	tmp_path.mkdir(parents=True, exist_ok=True)

	tmp_file = tmp_path / filename
	tmp_file.write_bytes(requests.get(archive_path).content)

	repo_path = tmp_path / filename.split(".")[0]
	repo_path.mkdir(exist_ok=True)

	tarfile.open(tmp_file).extractall(path=repo_path)
	return repo_path



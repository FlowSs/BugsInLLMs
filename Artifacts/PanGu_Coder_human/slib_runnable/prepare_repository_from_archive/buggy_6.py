def prepare_repository_from_archive(
    archive_path: str, filename: str, tmp_path: str
) -> str:
    uncompress_path = uncompress_file(archive_path, tmp_path)
    repo_url = get_repo_url(uncompress_path)
    return repo_url
def prepare_repository_from_archive(
    archive_path: str, repository_url: str = DEFAULT_REPOSITORY_URL
) -> str:
    archive = open_archive(archive_path)
    return prepare_repository_from_archive_data(archive, repository_url)

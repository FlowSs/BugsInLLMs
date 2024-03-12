def prepare_repository_from_archive(
    archive_path: Path, repository_url: str = None
) -> str:
    with Archive(archive_path, repository_url) as archive:
        return archive.prepare_repository()

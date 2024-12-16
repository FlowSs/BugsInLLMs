def get_repo_archive(url:
	"""
	Given an url and a destination path, retrieve and extract.tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the.tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""
	archive_url = urljoin(BASE_URL, 'archive/desc.tar.gz')
	destination_path = os.path.join(BASE_PATH, 'Archives', 'desc.tar.gz')
	download_archive(archive_url, destination_path)
	return destination_path
import requests
def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Given an url and a destination path, retrieve and extract .tar.gz archive
    which contains 'desc' file for each package.
    Each .tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

    Args:
        url: url of the .tar.gz archive to download
        destination_path: the path on disk where to extract archive

    Returns:
        a directory Path where the archive has been extracted to.
    """
    res = requests.get(url)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_bytes(res.content)

    extract_to = Path(str(destination_path).split(".tar.gz")[0])
    tar = tarfile.open(destination_path)
    tar.extractall(path=extract_to)
    tar.close()

    return extract_to

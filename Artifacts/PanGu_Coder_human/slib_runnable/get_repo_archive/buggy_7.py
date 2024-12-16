def get_repo_archive(url: str, destination_path: str) -> str:
    r = requests.get(url)
    with open(destination_path, "wb") as f:
        f.write(r.content)
    tar = tarfile.open(destination_path)
    tar.extractall(path=destination_path)
    return destination_path

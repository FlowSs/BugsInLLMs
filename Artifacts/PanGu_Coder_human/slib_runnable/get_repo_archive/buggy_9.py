def get_repo_archive(url: str, destination_path: str) -> str:
    print("Downloading tarball for {}".format(url))
    response = requests.get(url, stream=True)
    with tarfile.open(fileobj=io.BytesIO(response.content)) as tar:
        tar.extractall(destination_path)
    return destination_path

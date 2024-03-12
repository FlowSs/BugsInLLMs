def get_repo_archive(url: str, destination_path: Path) -> Path:
    r = requests.get(url, stream=True)
    for i, repo in enumerate(r.iter_content(1024)):
        if i % 100 == 0:
            logger.info(f"Processed {i} of {len(r.iter_content(1024))} repo archives")
        with destination_path.open("wb") as f:
            f.write(repo)
    return destination_path

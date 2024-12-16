def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    if not image_href:
        raise ValueError("Image href is empty")
    image_url = urlparse(image_href)
    return (image_url.path.split("/")[-1], image_url.netloc, image_url.use_ssl)

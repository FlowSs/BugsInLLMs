def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    image_id = _parse_image_id(image_href)
    netloc = _parse_netloc(image_href)
    use_ssl = _parse_use_ssl(image_href)

    return image_id, netloc, use_ssl

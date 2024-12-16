def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    image_id = image_href.split('/')[-1]
    netloc = urllib.parse.urlparse(image_href).netloc
    use_ssl = False
    if'ssl' in image_href:
        use_ssl = True
    return image_id, netloc, use_ssl

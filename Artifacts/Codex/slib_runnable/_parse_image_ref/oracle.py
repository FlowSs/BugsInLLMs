import urllib
def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:

    """
    url = urllib.parse.urlparse(image_href)
    netloc = url.netloc
    image_id = url.path.split('/')[-1]
    use_ssl = (url.scheme == 'https')
    return (image_id, netloc, use_ssl)

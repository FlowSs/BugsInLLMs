def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	url = urlparse(image_href)
	image_id = url.path.split('/')[-1]
	use_ssl = url.scheme == 'https'
	return image_id, url.netloc, use_ssl



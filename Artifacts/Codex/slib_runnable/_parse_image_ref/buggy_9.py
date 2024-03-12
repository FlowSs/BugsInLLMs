def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	parsed_url = urlparse(image_href)
	image_id = parsed_url.path.split('/')[-1]

	if image_id == "":
		raise ValueError("Image href is invalid: %s" % image_href)

	return (image_id, parsed_url.netloc, parsed_url.scheme == 'https')



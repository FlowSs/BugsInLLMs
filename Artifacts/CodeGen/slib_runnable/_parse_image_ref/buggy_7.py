def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	if not isinstance(image_href, str):
		raise ValueError("Invalid image_href")
	if not image_href.startswith("https"):
		raise ValueError("Invalid image_href")
	if not image_href.endswith("/"):
		raise ValueError("Invalid image_href")
	if not image_href.startswith("http"):
		raise ValueError("Invalid image_href")
	if image_href.endswith(".jpg") or image_href.endswith(".png"):
		return image_href.split("/")[0], None, None
	if image_href.endswith(".gif") or image_href.endswith(".jpeg") or image_href.endswith(".bmp"):
		return None, image_href.split("/")[0], True
	if image_href.endswith(".tif") or image_href.endswith(".tiff"):
		return image_href.split("/")[0], None, None
	if image_href.endswith(".png") or image_href.endswith(".jpg") or image_href.endswith(".jpeg"):
		return image_href.split("/")[0], image_href.split("/")[1], True
	if image_href.endswith(".gif") or image_href.endswith(".jpeg") or image_href.endswith(".bmp"):
		return image_href.split("/")[0], image_href.split("/")[1], False
	if image_href.endswith(".tif") or image_href.endswith(".tiff"):
		return image_href.split("/")[0], image_href.split("/")[1], False
	raise ValueError("Invalid image_href")


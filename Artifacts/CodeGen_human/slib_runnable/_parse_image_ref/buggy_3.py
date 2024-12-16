def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href:
		raise ValueError('Invalid image_href')

	return image_href.split('/')[-1].split('?')[0].split('?')[0].split('=')[0].split('/')[-1]
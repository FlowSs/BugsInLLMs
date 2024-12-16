def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if '/' in image_href:
		raise ValueError('invalid image_href:'+ image_href)

	if '/' not in image_href:
		raise ValueError('invalid image_href:'+ image_href)

	image_id = image_href.split('/')[-1]
	netloc = image_href.split('/')[0]
	use_ssl = 'https' in netloc
	return (image_id, netloc, use_ssl)


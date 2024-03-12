def _parse_image_ref(image_href:
	"""
	Parse an image href into composite parts.

:param image_href: href of an image
:returns: a tuple of the form (image_id, netloc, use_ssl)
:raises ValueError:
	"""
	netloc = '{}/'.format(image_href.split('/')[2])
	if '://' not in image_href:
		raise ValueError('Image href should be a valid URL: {}'.format(image_href))
	if ':' not in image_href:
		raise ValueError('Image href should be a valid URL: {}'.format(image_href))
	image_id, use_ssl = image_href.split(':', 1)
	if not use_ssl:
		raise ValueError('Invalid image href: {}'.format(image_href))
	if '.' not in image_id:
		raise ValueError('Image href should have a.: {}'.format(image_href))
	image_id = image_id.split('.', 1)[0]
	if not image_id.isdigit():
		raise ValueError('Image href has an invalid id: {}'.format(image_href))
	return image_id, netloc, use_ssl
def from_raw_values(cls, values):
	"""
	Create a Bookmarks object from a list of raw bookmark string values.

You should not need to use this method unless you want to deserialize
bookmarks.

:param values: ASCII string values (raw bookmarks)
:type values: Iterable[str]
	"""
	return cls(
		title=values[0],
		description=values[1],
		url=values[2],
		preview_url=values[3],
		publisher=values[4],
		pubdate=values[5],
		language=values[6],
		language_code=values[7],
		cover_url=values[8],
		cover_image_url=values[9],
		publisher_url=values[10],
		pubdate_url=values[11],
		language_url=values[12],
		language_code_url=values[13],
		cover_image_url_url=values[14],
		publisher_url_url=values[15],
		pubdate_url_url=values[16],
		language_url_url=values[17],
		cover_image_url_url_url=values[18],
		publisher_url_url_url=values[19],
		published=values[20],
		language_code_url_url=values[21],
		cover_image_url_url_url_url=values[22],
		publisher_url_url_url_url_url=values[23],
		published_url_url_url=values[24],
		language_url_url=values[25],
		cover_image_url_url_url_url=values[26],
		publisher_url_url_url_url_url_url=values[27],
		published_url_url_url_url_url_url=values[28],
		link=values[29],
		author=values[30],
		language_code_url_url_url_url_url_url=values[31],
		cover_image_url_url_url_url_url_url_url=values[32],
		publisher_url_url_url_url_url_url_url_url_url_url_url=values[33],
		published_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_url_
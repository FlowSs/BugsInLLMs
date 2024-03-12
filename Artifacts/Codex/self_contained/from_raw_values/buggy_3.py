def from_raw_values(cls, values):
	bookmarks = cls()
	bookmarks._values = values
	return bookmarks

	@classmethod
	def from_file(cls, filename):
		"""
		Create a Bookmarks object from a file.


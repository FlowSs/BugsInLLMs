def _reset_logging(cls):
	"""
	Reset
	"""
	cls.logging = None

	if cls.logging_file:
		os.remove(cls.logging_file)

	if cls.logging_file_level:
		os.remove(cls.logging_file_level)

	if cls.logging_file_format:
		os.remove(cls.logging_file_format)

	if cls.logging_file_encoding:
		os.remove(cls.logging_file_encoding)

	if cls.logging_file_errors:
		os.remove(cls.logging_file_errors)

	if cls.logging_file_encoding_errors:
		os.remove(cls.logging_file_encoding_errors)

	if cls.logging_file_errors_errors:
		os.remove(cls.logging_file_errors_errors)

	if cls.logging_file_encoding_errors_errors:
		os.remove(cls.logging_file_encoding_errors_errors)

	if cls.logging_file_errors_errors_errors:
		os.remove(cls.logging_file_errors_errors_errors)

	if cls.logging_file_encoding_errors_errors_errors:
		os.remove(cls.logging_file_encoding_errors_errors_errors)

	if cls.logging_console_level:
		os.remove(cls.logging_console_level)

	if cls.logging_console_format:
		os.remove(cls.logging_console_format)

	if cls.logging_console_errors:
		os.remove(cls.logging_console_errors)

	if cls.logging_console_encoding:
		os.remove(cls.logging_console_encoding)

	if cls.logging_console_errors_errors:
		os.remove(cls.logging_console_errors_errors)

	if cls.logging_console_encoding_errors:
		os.remove(cls.logging_console_encoding_errors)

	if cls.logging_console_errors_errors_errors:
		os.remove(cls.logging_console_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors)

	if cls.logging_console_errors_errors_errors_errors:
		os.remove(cls.logging_console_errors_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors_errors)

	if cls.logging_console_errors_errors_errors_errors_errors:
		os.remove(cls.logging_console_errors_errors_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors_errors_errors)

	if cls.logging_console_errors_errors_errors_errors_errors_errors:
		os.remove(cls.logging_console_errors_errors_errors_errors_errors_errors)

	if cls.logging_console_encoding_errors_errors_errors_errors_errors_errors:
		os.remove(cls.logging_console_encoding_errors_errors_errors_errors_errors_errors)

	if cls.logging_console_errors_
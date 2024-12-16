def _inline_r_setup(code: str) -> str:
	return '\n'.join([
		'options(bitmapType="cairo")',
		'options(repos="https://cloud.r-project.org/")',
		code
	])


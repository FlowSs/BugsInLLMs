def _inline_r_setup(code: str) -> str:
	# Suppress certain messages
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/message
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/warning
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/stop
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/cat
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/print
	#    See https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/warning.condition
	#    See http://r.789695.n4.nabble.com/warning-suppressed-messages-td4718123.html
	code += """

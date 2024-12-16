def _inline_r_setup(code: str) -> str:
	return (
		code
		+ """
		options(width=10000)
		options(error=function() {
			dev.off()
			stop(paste("R error:", geterrmessage()), call. = FALSE)
		})
		"""
	)



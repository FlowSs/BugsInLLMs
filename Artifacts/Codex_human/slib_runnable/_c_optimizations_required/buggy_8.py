def _c_optimizations_required():
	return os.environ.get("TEST_C_OPTIMIZATIONS", "1") == "1"


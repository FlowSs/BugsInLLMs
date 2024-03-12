    @classmethod
    def _reset_logging(cls):
        """
        Reset
        """

        # Found no way to fully reset the logging stuff while running
        # We reset root and all loggers to INFO, and kick handlers

        # Initialize
        root = logging.getLogger()
        root.setLevel(logging.getLevelName("INFO"))
        for h in root.handlers:
            # noinspection PyBroadException
            try:
                h.close()
            except:
                pass
        root.handlers = []

        # Browse all loggers and set
        for name in logging.root.manager.loggerDict:
            cur_logger = logging.getLogger(name)
            cur_logger.setLevel(logging.getLevelName("INFO"))
            for h in cur_logger.handlers:
                # noinspection PyBroadException
                try:
                    h.close()
                except:
                    pass
            cur_logger.handlers = []

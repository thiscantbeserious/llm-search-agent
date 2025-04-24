import logging


def get_logger(name: str = __name__) -> logging.Logger:
    """Return a configured logger for the given module/name."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        # first time config for this logger
        handler = logging.StreamHandler()
        fmt = "%(asctime)s %(levelname)4s [%(name)s] %(message)s"
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

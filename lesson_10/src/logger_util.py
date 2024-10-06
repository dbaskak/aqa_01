import logging


# Loger config
def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(message)s'
    )
    logger = logging.getLogger('log_event')
    logger.handlers = []
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

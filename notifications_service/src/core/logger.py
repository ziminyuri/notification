import logging

logger = logging.getLogger('ETL_logger')

logger.setLevel('INFO')

stream_handler = logging.StreamHandler()
logging_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
stream_handler.setFormatter(logging_format)

logger.addHandler(stream_handler)

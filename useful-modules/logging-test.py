import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.info('awesome')

# log to file
import logging.handlers
handler = logging.handlers.WatchedFileHandler('test.log')
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(handler)
logger.info('log to file')

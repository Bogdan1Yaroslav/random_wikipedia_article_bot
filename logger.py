import logging
from datetime import datetime

log_created_at = datetime.now().strftime("%d.%m.%Y")
log_format = '%(asctime)s %(filename)s: %(message)s'

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=f'logs/logs_dated_{log_created_at}.log')


def logger_info(function_name):
    logger.info(f"User has requested: '{function_name.__name__}'")

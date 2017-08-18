import os
import logging
import logging.handlers

# configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)8s - %(message)s')
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fmt)
# rotating file handler. Size of each file is 10M
log_file = os.path.join(os.path.dirname(__file__), 'xx.log')
rfh = logging.handlers.RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
rfh.setLevel(logging.INFO)
rfh.setFormatter(fmt)
logger.addHandler(ch)
logger.addHandler(rfh)

def main():
    logger = logging.getLogger(__name__)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    try:
        1/0
    except Exception as e:
        logger.exception('exception %s', e)
    logger.critical('critical')

if __name__ == '__main__':
    main()

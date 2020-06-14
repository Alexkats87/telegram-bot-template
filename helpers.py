import logging as log
from datetime import datetime

def set_logger(logger):
    
    NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    SUFFIX = str(NOW.replace('-', '').replace(':', '').replace(' ', '_'))
    LOG_FILE = 'telebot_' + SUFFIX + '.log'


    logger.basicConfig(level=logger.INFO,
                        format='%(asctime)s  %(levelname)-8s %(message)s',
                        datefmt='%y-%m-%d %H:%M',
                        filename=LOG_FILE,
                        filemode='w')

    return logger

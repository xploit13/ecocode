# logger.py
# Logging operations for EcoCode

import logging

def configure_logging():
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')
    return logging.getLogger('EcoCodeLogger')

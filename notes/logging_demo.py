'''
a few features of the logging module

Severity levels:

<-- less severe ..... more severe -->
DEBUG  INFO  WARNING  ERROR  CRITICAL

'''

import logging

LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR)

LOGGER.debug('some very detailed message')
LOGGER.info('the coffee-pot is brewing')
LOGGER.warning('waiting on network')
LOGGER.error('record malformed')
LOGGER.critical('the CPU is melting')

try:
    raise RuntimeError('I tripped')
except RuntimeError:
    LOGGER.exception('tripped')


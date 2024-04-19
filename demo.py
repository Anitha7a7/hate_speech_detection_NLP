import logging 
from hate import exception
import sys

logging.info('Adding 2 numbers')

try:
    2/0
except Exception as e:
    raise exception.CustomException(e, sys)

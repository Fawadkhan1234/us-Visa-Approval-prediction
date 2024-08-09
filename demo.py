from us_visa.logger import logging
from us_visa.exception import UsVisaException
import sys

try:
   a = 1/ "10"
except Exception as e:
   raise UsVisaException(e,sys) from e

#logging.info("welcom to our custom log")
import sys
from src.logger import logging
from src.exception import CustomException

try:
    a = 1 / 0
except Exception as e:
    logging.info("devide by zero error")
    raise CustomException(e, sys)
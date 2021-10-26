import logging
import os
import sys
import config as cf

request_file = os.path.join(cf.BASE_PATH, "logs", "request.log")
error_file = os.path.join(cf.BASE_PATH, "logs", "error.log")


def load_log():
    formatter1 = logging.Formatter("%(asctime)s : %(name)s - %(levelname)s - %(message)s", "%m/%d/%Y %I:%M:%S %p")
    formatter2 = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    logger = logging.getLogger("logger1")
    logger.setLevel(logging.DEBUG)
    '''handler 1'''
    handler1 = logging.FileHandler(request_file, mode="a")
    handler1.setLevel(logging.INFO)
    handler1.setFormatter(formatter1)
    '''Handler 2'''
    handler2 = logging.FileHandler(error_file, mode="a")
    handler2.setLevel(logging.ERROR)
    handler2.setFormatter(formatter2)
    '''Handler 3'''
    handler3 = logging.StreamHandler(sys.stdout)
    handler3.setLevel(logging.INFO)
    handler3.setFormatter(formatter1)
    '''Add handlers'''
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.addHandler(handler3)
    return logger
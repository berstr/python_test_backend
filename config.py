from flask import Flask

import os
import logging


PYTHON_TEST_BACKEND_PORT_DEFAULT = 8084

# ==========================
# The following variables are being set by the application at runtime:
# ==========================
APP = None
LOGGER = None


PYTHON_TEST_BACKEND_PORT = os.environ.get("PYTHON_TEST_BACKEND_PORT")
if (PYTHON_TEST_BACKEND_PORT == None):
    PYTHON_TEST_BACKEND_PORT=PYTHON_TEST_BACKEND_PORT_DEFAULT


# ==========================
# Init of variables, etc.
# ==========================

APP = Flask(__name__,static_folder='public', static_url_path='')


def init():
    init_logger()



def init_logger():
    global LOGGER
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(console_handler)

    LOGGER = logger



#!/usr/bin/env python

import os
import logging as log
from utils.common import LogManager

if __name__ == '__main__':
    print("RUNNING....")
    log_manager = LogManager()
    log_manager.init_logging()
    log.info("Hello World!")

    log.info("Environment: %s", os.environ)

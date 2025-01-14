#!/usr/bin/env python

from some_utility import tech_util

import os
import json
import logging as log
from utils.common import LogManager

if __name__ == '__main__':
    print("RUNNING....")
    log_manager = LogManager()
    log_manager.init_logging()
    log.info("Hello World!")
    log.info("Environment: %s", os.environ)

    result = {'result': tech_util.sum_n_multiply(2)}

    with open(os.environ['RESULT_FILE'], 'w', encoding="utf8") as target_file:
        target_file.write(json.dumps(result))

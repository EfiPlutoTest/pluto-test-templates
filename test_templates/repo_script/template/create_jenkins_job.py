#!/usr/bin/env python

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

    result = {'projectKey': os.environ['PROJECT_NAME'],
              'url': f"http://jenkins.example.com/{os.environ['PROJECT_NAME']}",
              'orgName': os.environ['SPROUT_ORG_NAME'],
              'projectName': os.environ['SPROUT_PROJECT_NAME'],
              'repoName': os.environ['SPROUT_REPO_NAME'],
              'repoUrl':  os.environ['SPROUT_REPO_URL']}

    with open(os.environ['RESULT_FILE'], 'w', encoding="utf8") as target_file:
        target_file.write(json.dumps(result))

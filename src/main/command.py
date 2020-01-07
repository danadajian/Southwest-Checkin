import subprocess
import logging
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run_command(command):
    command_list = re.split(r"\s+(?=[^()]*(?:\(|$))", command)
    try:
        logger.info("Running shell command: \"{}\"".format(command))
        result = subprocess.run(command_list, stdout=subprocess.PIPE)
        logger.info("Command output:\n---\n{}\n---".format(result.stdout.decode('UTF-8')))
    except Exception as e:
        logger.error("Exception: {}".format(e))

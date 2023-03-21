import random

import schedule
from subprocess import Popen
import time
import os
from config import *
import logging

logger = logging.getLogger()
logger.propagate = False

def analysis():
    Popen(['python', 'analysis.py'])


if __name__ == "__main__":
    analysis()
    schedule.every(1).hour.do(analysis)

    while True:
        schedule.run_pending()
        time.sleep(1)
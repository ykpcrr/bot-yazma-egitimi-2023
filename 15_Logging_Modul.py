import logging
import os
from datetime import datetime
import sys


# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="example.log",
#     filemode="w",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s "
# )

# Create log file if not exists

file = "./logs"
if not os.path.exists(file):
    os.mkdir(file)

# Create 2 type of log
# 1. log file for each day
# 2. write log on cmd

today = datetime.today().strftime("%Y.%m.%d")
file_log = logging.FileHandler(f"{file}/{today}.log", encoding="utf-8", mode="a")


cmd_log = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    handlers=[file_log, cmd_log],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",
    level=logging.DEBUG,
    datefmt="%Y.%m.%d - %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.debug("log level used by the developer during coding")
logger.info("Information log level")
logger.warning("warning log level")
logger.error("error log level")
logger.critical("error log level that can affect software operation at the highest level")

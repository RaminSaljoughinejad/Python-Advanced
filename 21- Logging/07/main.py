import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler("07\log.txt")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


x = 2
y = 0

try:
    print(x/y)
except:
    logger.exception("Exception occurred")

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler("06\mat.txt")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


"""logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s',
                    filename="05\mat.txt")"""

def cube(x):
    return x**3

def square(x):
    return x**2


x = 2
res1 = cube(x)
res2 = square(x)

logger.info('x = %s, res1 = %s, res2 = %s', x, res1, res2)
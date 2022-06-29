import logging
import mat

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(name)s - %(message)s',
                    filename="06\log.txt")

def greetings():
    return "Hello"

def farewell():
    return "Goodbye"


logging.debug(greetings())
logging.debug(farewell())
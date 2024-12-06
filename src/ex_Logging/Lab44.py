import logging

logging.basicConfig(filename="newfile2.log",
                    format='%(asctime)s %(message)s',
                    filemode="w")

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

x=3
y=0

logging.info(f"Values of x and y are: {x} and {y}")

try:
    x/y
    logging.info(f"x/y equals to {x/y}")
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError", exc_info=True)

logger.debug("Harmless debug message")
logger.info("It's just a information")
logger.warning("It's a warning")
logger.error("Did you divide by zero")
logger.critical("Internet is down")
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode="w")

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug message")
logger.info("Just a information")
logger.warning("It's a warning")
logger.error("Did you divide by zero")
logger.critical("Internet is down")
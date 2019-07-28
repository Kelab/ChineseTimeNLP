import logging
import sys

NLP_LOGGER = logging.getLogger("Time_NLP")
NLP_LOGGER.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(levelname)s: [%(filename)s %(funcName)s] > %(message)s")
handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)

NLP_LOGGER.addHandler(handler)

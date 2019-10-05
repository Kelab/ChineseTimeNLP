import logging
import sys

Time_NLP_LOGGER = logging.getLogger("Time_NLP")
Time_NLP_LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(levelname)s: [%(filename)s %(funcName)s] > %(message)s")
handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)

Time_NLP_LOGGER.addHandler(handler)

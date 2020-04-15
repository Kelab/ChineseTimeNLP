import sys

from loguru import logger

from .resource.pattern import r, pattern
from .normalizer import TimeNormalizer
from .helpers.StringPreHandler import StringPreHandler
from .helpers.LunarSolarConverter import LunarSolarConverter

logger.remove()
default_logger = logger.add(sys.stdout, level="INFO")


__all__ = [
    "TimeNormalizer",
    "StringPreHandler",
    "LunarSolarConverter",
    "default_logger",
    "pattern",
    "r",
]

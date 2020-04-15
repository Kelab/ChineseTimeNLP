import sys

from loguru import logger

from .resource.pattern import r, pattern
from .LunarSolarConverter import LunarSolarConverter
from .StringPreHandler import StringPreHandler
from .normalizer import TimeNormalizer

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

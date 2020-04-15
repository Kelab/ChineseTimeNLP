import sys
from loguru import logger

from .resource.pattern import r, pattern
from .normalizer import TimeNormalizer
from .helpers.LunarSolarConverter import LunarSolarConverter
from .helpers import int_common, str_common

logger_format = "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.remove()
default_logger = logger.add(sys.stdout, format=logger_format, level="INFO")


__all__ = [
    "TimeNormalizer",
    "int_common",
    "str_common",
    "LunarSolarConverter",
    "default_logger",
    "logger_format",
    "pattern",
    "r",
]

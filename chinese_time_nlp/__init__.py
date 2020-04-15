import sys
from loguru import logger

from .resource.pattern import r, pattern
from .normalizer import TimeNormalizer
from .helpers.LunarSolarConverter import LunarSolarConverter
from .helpers import int_common, str_common

logger.remove()
default_logger = logger.add(
    sys.stdout, format="{level}|{file} <red>{message}</>", level="INFO"
)


__all__ = [
    "TimeNormalizer",
    "int_common",
    "str_common",
    "LunarSolarConverter",
    "default_logger",
    "pattern",
    "r",
]

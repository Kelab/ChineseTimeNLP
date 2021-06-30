from typing import TYPE_CHECKING, List, Literal, Tuple, TypedDict

from loguru import logger

if TYPE_CHECKING:
    from .unit import TimeUnit  # noqa: F401


class DeltaType(TypedDict):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int


class Result(dict):
    @staticmethod
    def from_invalid() -> "Error":
        return Error(error="no time pattern could be extracted.")

    @staticmethod
    def from_exception(e: Exception) -> "Error":
        return Error(error=str(e))

    @staticmethod
    def from_timedelta(delta_dict: DeltaType) -> "Delta":
        logger.debug(f"time_delta: {delta_dict}")
        return Delta(delta_dict)

    @staticmethod
    def from_timestamp(result: List["TimeUnit"]) -> "Stamp":
        return Stamp(result[0].time.format("YYYY-MM-DD HH:mm:ss"))

    @staticmethod
    def from_timespan(result: List["TimeUnit"]) -> "Span":
        return Span(
            timespan=[
                result[0].time.format("YYYY-MM-DD HH:mm:ss"),
                result[1].time.format("YYYY-MM-DD HH:mm:ss"),
            ]
        )

    @property
    def type(
        self,
    ) -> Tuple[
        Literal["error"],
        Literal["timestamp"],
        Literal["timedelta"],
        Literal["timespan"],
    ]:
        """
        结果类型，有 ``error``、``timespan``、``timedelta``、``timestamp``。
        """
        return self["type"]


class Error(Result):
    __slot__ = "type", "error"

    def __init__(self, error) -> None:
        self["type"] = "error"
        self["error"] = error


class Delta(Result):
    __slot__ = "type", "timedelta"

    def __init__(self, timedelta: DeltaType) -> None:
        self["type"] = "timedelta"
        self["timedelta"] = timedelta


class Stamp(Result):
    __slot__ = "type", "timestamp"

    def __init__(self, timestamp: str) -> None:
        self["type"] = "timestamp"
        self["timestamp"] = timestamp


class Span(Result):
    __slot__ = "type", "timespan"

    def __init__(self, timespan) -> None:
        self["type"] = "timespan"
        self["timespan"] = timespan

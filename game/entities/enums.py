from enum import StrEnum, auto


class TaskStatus(StrEnum):
    close = auto()
    open = auto()
    enter = auto()

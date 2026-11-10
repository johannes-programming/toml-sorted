from __future__ import annotations

__all__: list[str] = ["Selector"]

import enum


class Selector(enum.Enum):
    ALL_KEYS = enum.auto()
    ALL_INDICES = enum.auto()

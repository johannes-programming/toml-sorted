from __future__ import annotations

__all__: list[str] = ["Instruction"]

import enum


class Instruction(enum.Enum):
    SORT = False
    SORT_REVERSE = True

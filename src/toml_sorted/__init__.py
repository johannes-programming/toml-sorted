from __future__ import annotations

__all__: list[str] = ["Instruction", "Selector", "main", "parse_args", "run"]

import sys

from toml_sorted.core.main import main
from toml_sorted.core.parse_args import parse_args
from toml_sorted.core.run import run
from toml_sorted.enum.Instruction import Instruction
from toml_sorted.enum.Selector import Selector

if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

__all__: list[str] = ["parse_args"]


import argparse
from collections.abc import Iterable

from toml_sorted.enum.Instruction import Instruction
from toml_sorted.enum.Selector import Selector


def parse_args(args: Iterable[str] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    parser = argparse.ArgumentParser(fromfile_prefix_chars="@")
    parser.add_argument(
        "--all-indices",
        action="append_const",
        const=Selector.ALL_INDICES,
        dest="instructions",
    )
    parser.add_argument(
        "--all-keys",
        action="append_const",
        const=Selector.ALL_KEYS,
        dest="instructions",
    )
    parser.add_argument(
        "--index",
        action="append",
        dest="instructions",
        type=int,
    )
    parser.add_argument(
        "--key",
        action="append",
        dest="instructions",
    )
    parser.add_argument(
        "--sort",
        action="append_const",
        const=Instruction.SORT,
        dest="instructions",
    )
    parser.add_argument(
        "--sort-reverse",
        action="append_const",
        const=Instruction.SORT_REVERSE,
        dest="instructions",
    )
    parser.add_argument(
        "filepatterns",
        nargs="*",
        default=[],
    )
    parser.set_defaults(instructions=[])
    return parser.parse_args(args)

from __future__ import annotations

__all__: list[str] = ["main"]


import argparse
import logging
from collections import abc
from typing import Any

from toml_sorted.core.parse_args import parse_args
from toml_sorted.core.run import run


def main(args: abc.Iterable[str] | None = None) -> int:
    filepatterns: abc.Sequence[str]
    kwargs: dict[str, Any]
    space: argparse.Namespace
    try:
        space = parse_args(args)
        kwargs = vars(space)
        filepatterns = kwargs.pop("filepatterns")
        run(*filepatterns, **kwargs)
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return int(exit.code)
        else:
            return int(bool(exit.code))
    except BaseException as exc:
        logging.exception(exc)
        return 1
    else:
        return 0

from __future__ import annotations

__all__: list[str] = ["TestTomlSort"]


import io
import tempfile
import tomllib
import unittest
from pathlib import Path
from typing import Any, Self

import tomli_w

from toml_sorted.core.run import run
from toml_sorted.enum.Instruction import Instruction


class TestTomlSort(unittest.TestCase):

    def test_run_sorts_matching_toml_file(self: Self, /) -> None:
        path: Path
        result: dict[str, Any]
        stream: io.BufferedWriter
        tmpdir: str
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "example.toml"
            with path.open("wb") as stream:
                tomli_w.dump({"b": 2, "a": 1}, stream)
            run(
                str(path),
                instructions=[Instruction.SORT],
            )
            with path.open("rb") as stream:
                result = tomllib.load(stream)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_run_ignores_duplicate_glob_matches(self: Self, /) -> None:
        path: Path
        result: dict[str, Any]
        stream: io.BufferedWriter
        tmpdir: str
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "example.toml"
            with path.open("wb") as stream:
                tomli_w.dump({"b": 2, "a": 1}, stream)
            run(
                str(path),
                str(path),
                instructions=[Instruction.SORT],
            )
            with path.open("rb") as stream:
                result = tomllib.load(stream)
        self.assertEqual(result, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()

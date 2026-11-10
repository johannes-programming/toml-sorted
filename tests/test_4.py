from __future__ import annotations

__all__: list[str] = ["TestRunNoMatch"]


import contextlib
import io
import unittest
from typing import Self

from toml_sorted.core.run import run
from toml_sorted.enum.Instruction import Instruction


class TestRunNoMatch(unittest.TestCase):

    def test_run_warns_when_no_files_matched(self: Self, /) -> None:
        err: io.StringIO
        with contextlib.redirect_stderr(err := io.StringIO()):
            run(
                "does-not-exist-*.toml",
                instructions=[Instruction.SORT],
            )
        self.assertIn("no files matched", err.getvalue())


if __name__ == "__main__":
    unittest.main()

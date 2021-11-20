"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import io
from textwrap import dedent
from unittest import main, TestCase
from unittest.mock import patch
from typing import List

from solution import _main


def _process_input(s1: str, s2: str) -> List[tuple]:
    s1 = tuple(map(int, s1.split()))
    s2 = tuple(map(int, s2.split()))
    return s1[:2], s1[2:], s2[:2], s2[2:]


class TestCase(TestCase):

    data = (
        ("1 1 3 4", "2 3 6 7", "21\n"),
        ("0 0 2 2", "2 2 4 4", "8\n"),
        ("1 1 4 3", "2 4 7 6", "16\n"),
        ("1 1 2 2", "4 3 5 4", "2\n"),
        ("0 0 5 3", "1 1 4 2", "15\n"),
        ("1 1 4 5", "2 1 6 5", "20\n"),
        ("1 1 6 5", "2 2 5 4", "20\n"),
        ("1 1 5 4", "2 2 5 4", "12\n"),
        ("1 1 5 5", "2 2 7 4", "20\n"),
        ("2 1 5 2", "2 4 4 5", "5\n"),
        ("5 1 7 3", "1 1 4 5", "16\n"),
        ("5 1 7 3", "4 5 1 1", "16\n"),
        ("1 1 4 5", "5 1 7 3", "16\n"),
        ("4 5 1 1", "7 3 5 1", "16\n"),
    )
    
    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(
        self,
        expected_output,
        mock_output, 
        function=None,
        args=None,
    ):
        if function:
            function(args)
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_solvers(self):
        for s1, s2, total_area in self.data:
            self.assert_stdout(
                total_area,
                function=_main,
                args=_process_input(s1, s2),
            )


if __name__ == "__main__":
    main()
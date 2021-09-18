"""
Given a list of numbers, stop processing input after the cumulative sum
of all the input becomes negative.

Input format: A list of integers to be processed
Constrains: All numbers input are integers between -1000 and 1000
Output format: Print all the numbers before the cumulative sum become
negative.

Sample Input
1
2
88
-100
49

Sample Output
1
2
88
"""
import io
from textwrap import dedent
from unittest import main, TestCase
from unittest.mock import patch


data = [1, 2, 88, -100, 49]


def solution():
    s = 0
    for n in data:
        s += n
        if s < 0:
            return None
        print(n)


class Test(TestCase):
    
    output = """\
    1
    2
    88
    """

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_solution(self):
        self.assert_stdout(dedent(self.output), function=solution)


if __name__ == "__main__":
    main()
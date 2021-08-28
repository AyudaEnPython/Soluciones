"""
Book Titles

You have been asked to make a special book categorization program, which assigns
each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of 
characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12
characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written
on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12

file = open("/usercode/files/books.txt", "r")
#your code goes here
file.close()
"""
import io
from textwrap import dedent
from unittest import main, TestCase
from unittest.mock import patch

def solution_1():
    with open("books.txt", "r") as f: #change to "/usercode/files/books.txt"
        for book in f.read().splitlines():
            print(f"{book[0]}{len(book)}")

def solution_2():
    with open("books.txt", "r") as f: #change to "/usercode/files/books.txt"
        for book in f:
            book = book.replace("\n", "")
            print(f"{book[0]}{len(book)}")

def solution_3():
    file = open("books.txt", "r")  #change to "/usercode/files/books.txt"
    books = file.read().splitlines()
    for book in books:
        print(f"{book[0]}{len(book)}")
    file.close()

class Test(TestCase):
    books = """\
    H12
    T16
    P19
    G18
    """
    
    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)
        
    def test_solution(self):
        self.assert_stdout(dedent(self.books), function=solution_1)
        self.assert_stdout(dedent(self.books), function=solution_2)
        self.assert_stdout(dedent(self.books), function=solution_3)


if __name__ == "__main__":
    main()
"""
Title Encoder
=============

You are given a file named "books.txt" with book tiles, each on a
separate line.

To encode the book titles you need to take the first letters of each
word in the title and combine them.
For example, for the book title "Games of Thrones" the encoded version
should be "GoT".

Complete the program to read the book title from the file and output
the encoded versions, each on a new line.

Hint:
You can use the .split() method to get a list of words in a string.
"""

file = open("/usercode/files/books.txt", "r")
for line in  file.readlines():
    print("".join([s[0] for s in line.split()]))
file.close()

# with open("/usercode/files/books.txt", "r") as f:
#     for line in  f.readlines():
#         print("".join([s[0] for s in line.split()]))

"""
Simple Metacharacters
=====================

Write a program that takes a word as input, and outputs "Match" if the word
has 4 letters, stars with "m" and ends with "e".
The program should output "No match" if these mentioned requirements aren't
satisfied.

Sample Input:
mine

Sample Output:
Match
"""
import re

word = input()
pattern = r"^m..e$"
if re.match(pattern, word):
    print("Match")
else:
    print("No match")

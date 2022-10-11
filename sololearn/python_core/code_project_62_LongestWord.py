"""
Longest Word
============

Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

NOTE: Recall the split('') method, which returns a list of words of the
string.
"""

txt = input()
words = txt.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

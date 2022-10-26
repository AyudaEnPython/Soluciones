"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Write a "for" loop that will print 'pbil' when 'alphabetical' is the
input using Python.

This question actually expects the for loop to loop through the
string "alphabetical", and print out the characters p, b, i, l one by
one while looping.
"""

word = "alphabetical"
for i in range(2, len(word), 3):
    print(word[i])

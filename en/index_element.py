"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speak
"""

numbers = [50, 30, 20, 50, 50, 62, 70, 50]

# just the first match
print("Index ->", numbers.index(50))
# output: Index -> 0

# all matches
print("Indexes ->", list((i for i, el in enumerate(numbers) if el == 50)))
# output: Indexes -> [0, 3, 4, 7]
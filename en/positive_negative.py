"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""

numbers = [-402, 451, 7, -26, 365, -12, 11, -666, -1, 36]

positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))

print("Positive ->", positive)
# output: Positive -> [451, 7, 365, 11, 36]

print("Negative ->", negative)
# output: Negative -> [-402, -26, -12, -666, -1]
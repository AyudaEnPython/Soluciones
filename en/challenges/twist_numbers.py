"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - TWIST NUMBERS **

Print out the reverse of the number with each digit doubled.
Example: 426 -> (reverse) 624 -> (double) 1248

numbers = [34, 243, 659, 517, 8, 47]

# output
'The twisted numbers are: 86, 684, 181012, 14210, 1, 148'
"""

numbers = [34, 243, 659, 517, 8, 47]
twisted = map(
    lambda x: "".join(str(int(s)*2) for s in x),
    map(lambda x: x[::-1], map(str, numbers))
)

print(f"The twisted numbers are: {', '.join(twisted)}")

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - HAMMING DISTANCE **

Your company wants to start analyzing text-strings. As first step 
your boss has heard of Hamming distances and wants you to create 
code to calculate them. Hamming Distance: Number of positions at 
which corresponding symbols are different, a==b =>0, a!=b =>1  
Example: TIME and MINE => 1+0+1+0 = 2

words = ['peace','piece','geese','tease','spoon']
# output results in pairs or matrix format
output =[
    ['Ham-Dis', 'peace', 'piece', 'geese', 'tease', 'spoon'],
    ['peace', 0, 2, 3, 2, 5],
    ['piece', 2, 0, 3, 4, 5],
    ['geese', 3, 3, 0, 2, 5],
    ['tease', 2, 4, 2, 0, 5],
    ['spoon', 5, 5, 5, 5, 0]
]
# alt output : 'peace-piece:2, peace-geese:3...etc'

# Bonus: Amaze your boss and suggest a different way to compare strings
"""
from pandas import DataFrame


def distance(a: str, b: str) -> int:
    assert len(a) == len(b)
    return sum(p != q for p, q in zip(a, b))


words = ['peace','piece','geese','tease','spoon']
output = [[distance(a, b) for a in words] for b in words]

df = DataFrame(output, index=words, columns=words)
print(df)

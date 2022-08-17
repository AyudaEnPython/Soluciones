# 12.18. Chapter Assessment

Write a function called `int_return` that takes an integer as input and returns
the same integer.
```python
def int_return(x):
    return x
```

Write a function called `add` that takes any number as its input and returns
that sum with 2 added.
```python
def add(x):
    return x + 2
```

Write a function called `change` that takes any string, adds “Nice to meet you!”
to the end of the argument given, and returns that new string.
```python
def change(s):
    return s + "Nice to meet you!"
```

Write a function, `accum`, that takes a list of integers as input and returns
the sum of those integers.
```python
def accum(xs):
    return sum(xs)
```

Write a function, `length`, that takes in a list as the input. If the length of
the list is greater than or equal to 5, return “Longer than 5”. If the length is
less than 5, return “Less than 5”.
```python
def length(xs):
    return "Longer than 5" if len(xs) >= 5 else "Less than 5"
```

You will need to write two functions for this problem. The first function, `divide`
that takes in any number and returns that same number divided by 2. The second
function called `sum` should take any number, divide it by 2, and add 6. It should
return this new number. You should call the `divide` function within the `sum`
function. Do not worry about decimals.
```python
def divide(x):
    return x/2


def sum(x):
    return divide(x) + 6
```

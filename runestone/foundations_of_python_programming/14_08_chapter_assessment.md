# 14.8. Chapter Assessment

Write a function, `sublist`, that takes in a list of numbers as the parameter.
In the function, use a while loop to return a sublist of the input list. The
sublist should contain the same values of the original list up until it reaches
the number 5 (it should not contain the number 5).
```python
def sublist(xs):
    tmp = []
    i = 0
    while i != len(xs):
        if xs[i] == 5:
            break
        tmp.append(xs[i])
        i += 1
    return tmp
```

Write a function called `check_nums` that takes a list as its parameter, and
contains a while loop that only stops once the element of the list is the
number 7. What is returned is a list of all of the numbers up until it reaches 7.
```python
def check_nums(xs):
    tmp = []
    i = 0
    while i != len(xs):
        if xs[i] == 7:
            break
        tmp.append(xs[i])
        i += 1
    return tmp
```

Write a function, `sublist`, that takes in a list of strings as the parameter.
In the function, use a while loop to return a sublist of the input list. The
sublist should contain the same values of the original list up until it reaches
the string “STOP” (it should not contain the string “STOP”).
```python
def sublist(ss):
    tmp = []
    i = 0
    while i != len(ss):
        if ss[i] == "STOP":
            break
        tmp.append(ss[i])
        i += 1
    return tmp
```

Write a function called `stop_at_z` that iterates through a list of strings.
Using a while loop, append each string to a new list until the string that
appears is “z”. The function should return the new list.
```python
def stop_at_z(ss):
    tmp = []
    i = 0
    while i != len(ss):
        if ss[i] == "z":
            break
        tmp.append(ss[i])
        i += 1
    return tmp
```

Below is a for loop that works. Underneath the for loop, rewrite the problem so
that it does the same thing, but using a while loop instead of a for loop. Assign
the accumulated total in the while loop code to the variable `sum2`. Once complete,
sum2 should equal sum1.
```python
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0

i = 0
while i != len(lst):
    sum2 += lst[i]
    i += 1
```

**Challenge**: Write a function called `beginning` that takes a list as input and
contains a while loop that only stops once the element of the list is the string
‘bye’. What is returned is a list that contains up to the first 10 strings,
regardless of where the loop stops. (i.e., if it stops on the 32nd element, the
first 10 are returned. If “bye” is the 5th element, the first 4 are _returned_.)
_If you want to make this even more of a challenge, do this without slicing_
```python
def beginning(ss):
    tmp = []
    i = 0
    while i != len(ss):
        if ss[i] == "bye":
            break
        tmp.append(ss[i])
        i += 1
    if len(tmp) < 10:
        return tmp
    else:
        return [tmp[x] for x in range(10)]
```

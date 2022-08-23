# 17.09. Chapter Assessment

The variable nested contains a `nested` list. Assign ‘snake’ to the variable `output` using indexing.
```python
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
```

Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.
```python
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = "yellow" in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange =  "orange" in lst[0]
```

Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

```python
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = "hola" in L
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]
```

Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
```python
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = True if "data" in nested else False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = True if 24 in nested["data"] else False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = True if "whole" in nested else False
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = True if "physics" in nested else False 
```

The variable `nested_d` contains a nested dictionary with the gold medal counts for
the top four countries in the past three Olympics. Assign the value of Great
Britain’s gold medal count from the London Olympics to the variable `london_gold`.
Use indexing. Do not hardcode.
```python
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d["London"]["Great Britain"]
```

Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.
```python
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports["swimming"][2]
# Assign the string 'platform' to the name v2
v2 = sports["diving"][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports["gymnastics"]["women"]
# Assign the string 'rings' to the name v4
v4 = sports["gymnastics"]["men"][-1]
```

Given the dictionary, `nested_d`, save the medal count for the USA from all three Olympics in the dictionary to the list `US_count`.
```python
US_count = [v["USA"] for k, v in nested_d.items() for v_ in v if v_ == "USA"]
```

Iterate through the contents of `l_of_l` and assign the third element of sublist to a new list called `third`.
```python
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = [e[2] for e in l_of_l]
```

Given below is a list of lists of athletes. Create a list, `t`, that saves only the athlete’s
name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete
name into list `other`.
```python
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = [n for a in athletes for n in a if "t" in n]
other = [n for a in athletes for n in a if "t" not in n]
```

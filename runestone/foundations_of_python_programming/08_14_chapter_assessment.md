# 8.14. Chapter Assessment

`rainfall_mi` is a string that contains the average number of inches of rainfall
in Michigan for every month (in inches) with every month separated by a comma.
Write code to compute the number of months that have more than 3 inches of
rainfall. Store the result in the variable `num_rainy_months`. In other words,
count the number of items with values `> 3.0`.

Hard-coded answers will receive no credit.
```python
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = sum(1 for e in rainfall_mi.split(", ") if float(e) > 3.0)
```

The variable `sentence` stores a string. Write code to determine how many words in
`sentence` start and end with the same letter, including one-letter words. Store
the result in the variable `same_letter_count`.

Hard-coded answers will receive no credit.
```python
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count = sum(1 for w in sentence.split(" ") if w[0] == w[-1] or len(w) == 1)
```

Write code to count the number of strings in list `items` that have the character
`w` in it. Assign that number to the variable `acc_num`.

HINT 1: Use the accumulation pattern!

HINT 2: the `in` operator checks whether a substring is present in a string.

Hard-coded answers will receive no credit.
```python
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = sum(1 for item in items if "w" in item)
```

Write code that counts the number of words in `sentence` that contain either an
“a” or an “e”. Store the result in the variable `num_a_or_e`.

Note 1: be sure to not double-count words that contain both an a and an e.

HINT 1: Use the `in` operator.

HINT 2: You can either use `or` or `elif`.

Hard-coded answers will receive no credit.
```python
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = sum(1 for w in sentence.split(" ") if "a" in w or "e" in w)
```

Write code that will count the number of vowels in the sentence `s` and assign the
result to the variable `num_vowels`. For this problem, vowels are only a, e, i, o,
and u. Hint: use the `in` operator with `vowels`.
```python
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = sum(1 for w in s if w in vowels)
```

Create one conditional so that if “Friendly” is in `w`, then “Friendly is here!”
should be assigned to the variable `wrd`. If it’s not, check if “Friend” is in `w`.
If so, the string “Friend is here!” should be assigned to the variable `wrd`,
otherwise “No variation of friend is in here.” should be assigned to the
variable `wrd`. (Also consider: does the order of your conditional statements
matter for this problem? Why?)
```python
w = "Friendship is a wonderful human experience!"
if "Friendly" in w:
    wrd = "Friendly is here!"
elif "Friend" in w:
    wrd = "Friend is here!"
else:
    wrd = "No variation of friend is in here"
```

We have written conditionals for you to use. Create the variable x and assign
it some integer so that at the end of the code, `output` will be assigned the
string `"Consistently working"`.
```python
x = 8
if x >= 10:
    output = "working"
else:
    output = "Still working"
if x > 12:
    output = "Always working"
elif x < 7:
    output = "Forever working"
else:
    output = "Consistently working"
```

Write code so that if `"STATS 250"` is in the list `schedule`, then the string
`"You could be in Information Science!"` is assigned to the variable `resp`.
Otherwise, the string `"That's too bad."` should be assigned to the variable `resp`.
```python
schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]
resp = "You could be in Information Science!" if "STATS 250" in schedule else "That's too bad."
```

Create the variable `z` whose value is `30`. Write code to see if `z` is greater
than `y`. If so, add 5 to `y`’s value, otherwise do nothing. Then, multiply `z`
and `y`, and assign the resulting value to the variable `x`.
```python
y = 22
z = 30
y += 5 if z > y else 0
x = z * y
```

For each string in `wrd_lst`, find the number of characters in the string. If the
number of characters is less than 6, add 1 to `accum` so that in the end, `accum`
will contain an integer representing the total number of words in the list
that have fewer than 6 characters.
```python
wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
accum = sum(1 for w in wrd_lst if len(w) < 6)
```

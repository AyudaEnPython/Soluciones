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

```python
```

```python
```

```python
```
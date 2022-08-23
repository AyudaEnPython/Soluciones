# 16.09. Chapter Assessment

Sort the following string alphabetically, **from z to a**, and assign it
to the variable `sorted_letters`.
```python
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)
```

Sort the list below, `animals`, into alphabetical order, a-z. Save the new
list as `animals_sorted`.
```python
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
```

Write code to rearrange the strings in the list `winners` so that they are in
alphabetical order by first name from A to Z.
```python
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
```

Write code to switch the order of the `winners` list so that it is now Z to A, by
first name. Assign this list to the variable `z_winners`.
```python
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = sorted(winners, reverse=True)
```

Write code to switch the order of the `winners` list so that it is now A to Z by
last name. Assign this list to the variable `z_winners`.
```python
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = sorted(winners, key=lambda x: x.split(" ")[-1])
```

The dictionary, `medals`, shows the medal count for six countries during the Rio Olympics.
Sort the country names so they appear alphabetically. Save this list to the variable `alphabetical`.
```python
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(country for country in medals)
```

Given the same dictionary, `medals`, now sort by the medal count. Save the three countries
with the highest medal count to the list, `top_three`.
```python
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = [x for x, _ in sorted(medals.items(), key=lambda x: x[1], reverse=True)[:3]]
```

We have provided the dictionary `groceries`. You should return a list of its keys, but they
should be sorted by their values, from highest to lowest. Save the new list as `most_needed`.

```python
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = [x for x, _ in sorted(groceries.items(), key=lambda x: x[1])][::-1]
```

Create a function called `last_four` that takes in a single ID number and returns the last four
digits. For example, the number 17573005 should return 3005. Then, use the resulting function
to sort the list of ids stored in the variable, `ids`, from lowest to highest. Save this sorted
list in the variable, `sorted_ids`. Hint: Remember that only strings can be indexed, so
conversions may be needed.

```python
def last_four(x):
    return str(x)[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=lambda x: last_four(x))
```

Sort the list `ids` by the last four digits of each id. Do this using lambda and not using a
defined function. Save this sorted list in the variable `sorted_id`.

```python
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: str(x)[-4:])
```

Sort the following list by each element's second letter a to z. Do so by using lambda. Assign
the resulting value to the variable `lambda_sort`.

```python
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda x: x[1])
```

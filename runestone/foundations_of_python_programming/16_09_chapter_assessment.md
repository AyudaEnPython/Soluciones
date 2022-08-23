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
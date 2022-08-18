# 13.8. Chapter Assessment

Create a tuple called `olympics` with four elements: "Beijing", "London", "Rio",
"Tokyo".
```python
olympics = "Beijing", "London", "Rio", "Tokyo"
```

The list below, `tuples_lst`, is a list of tuples. Create a list of the second
elements of each tuple and assign this list to the variable `country`.
```python
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = [e[1] for e in tuples_lst]
```
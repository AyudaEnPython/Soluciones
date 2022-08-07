# 10.15. Chapter Assessment

The textfile, `travel_plans.txt`, contains the summer travel plans for someone with
some commentary. Find the total number of characters in the file and save to the
variable `num`.
```python
num = 0
with open("travel_plans.txt") as f:
    for line in f:
        for char in line:
            num += 1

# with open("travel_plans.txt") as f:
#     data = f.readlines()
# num = len([c for line in data for c in line])
```

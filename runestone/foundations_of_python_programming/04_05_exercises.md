# 4.5. Exercises

Use a `for` statement to print 10 random numbers.

```python
from random import random 

for _ in range(10):
    print(random())
```

Repeat the above exercise but this time to print 10
numbers between 25 and 35.
```python
from random import randint

for _ in range(10):
    print(randint(25, 35))
```

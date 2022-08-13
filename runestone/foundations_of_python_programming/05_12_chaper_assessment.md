# 5.12. Chapter Assessment - Drawing with Turtle

Write code to draw a regular pentagon (a five-sided figure with all sides the same length).
```python
import turtle

t = turtle.Turtle()
n, x = 5, 50
for _ in range(n):
    t.fd(x)
    t.lt(360/n)
```

Write a program that uses the turtle module to draw something. It doesn’t have
to be complicated, but draw something different than we have done in the past.
(Hint: if you are drawing something complicated, it could get tedious to watch
it draw over and over. Try setting `.speed(10)` for the turtle to draw fast, or
`.speed(0)` for it to draw super fast with no animation.)
```python

import turtle

t = turtle.Turtle()
n, x = 100, 2
for _ in range(n):
    t.fd(x)
    t.lt(360/n)
```

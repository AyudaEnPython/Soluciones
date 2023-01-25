# Missions

## Multiply (Intro)

Write a function that will receive 2 numbers as input and it should return the
multiplication of these 2 numbers.

**Input:** Two arguments. Both are type `int`.

**Output:** Int.

**Examples:**

```python
assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0
```

---

## Solution

```python
def mult_two(a: int, b: int) -> int:
    return a * b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")

```
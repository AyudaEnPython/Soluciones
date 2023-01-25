
Nicola likes to categorize all sorts of things. He categorized a series
of numbers and as the result of his efforts, a simple sequence of
numbers became a deeply-nested list. Sophia and Stephan don't really
understand his organization and need to figure out what it all means.
They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may
contain yet more lists and integers which then… you get the idea. You
should put all of the integer values into one flat list. The order
should be as it was in the original list with string representation
from left to right.

We need to hide this program from Nikola by keeping it small and easy
to hide. Because of this, your code should be shorter than 140
characters (with whitespaces).

**Input:** A nested list of integers.

**Output:** List or another iterable (tuple, generator, iterator) of
integers.

**Example:**

```python
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]
```

**How it is used:** This concept is useful for parsing and analyzing
files with complex structures and the task challenges your creativity
in writing short code.

**Precondition:**
- 0 ≤ |array| ≤ 100
- ∀ x ∈ array : $-2^{32} < x < 2^{32}$ or x is a list
- depth < 10

## Solution

```python
from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    array = str(array).replace('[', '').replace(']', '').replace(',', '').strip()
    return list(map(int, array.split(' '))) if array else []


print("Example:")
print(list(flat_list([1, 2, 3])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")

```

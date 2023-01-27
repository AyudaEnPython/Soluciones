## Goes right after

In a given word you need to check if one symbol goes only right after
another.

Cases you should expect while solving this challenge:

- one of the symbols is not in the given word - your function should
return False;
- any symbol appears in a word more than once - use only the first one
- two symbols are the same - your function should return False
- the condition is case sensitive, which means 'a' and 'A' are two different symbols.


**Input:** Three arguments. The first one is a given string, second is
a symbol that should go firts, and the third is a symbol that should
go after the first one.

**Output:** A bool.

**Example:**

```python
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
```

## Solution

```python
def goes_after(word: str, first: str, second: str) -> bool:
    if (
        not word or first == second or 
        (first not in word or second not in word)
    ):
        return False
    t = [x for x in word if word.count(x) > 1]
    x = 0 if not t else word.index(t[0])
    return word[x] == first and word[x + 1] == second


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

```

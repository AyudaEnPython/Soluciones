# 10.15. Chapter Assessment

The textfile, `travel_plans.txt`, contains the summer travel plans for someone
with some commentary. Find the total number of characters in the file and save
to the variable `num`.
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

We have provided a file called `emotion_words.txt` that contains lines of words
that describe emotions. Find the total number of words in the file and assign
this value to the variable `num_words`.
```python
num_words = 0
with open("emotion_words.txt") as f:
    for line in f:
        num_words += len(line.split(" "))

# with open("emotion_words.txt") as f:
#     num_words = sum(len(line.split(" ")) for line in f.readlines())
```

Assign to the variable `num_lines` the number of lines in the file
`school_prompt.txt`.
```python
num_lines = 0
with open("school_prompt.txt") as f:
    for line in f:
        num_lines += 1

# with open("school_prompt.txt") as f:
#     num_lines = len(f.readlines())
```

Assign the first 30 characters of `school_prompt.txt` as a string to the variable
`beginning_chars`.
```python
with open("school_prompt.txt") as f:
    beginning_chars = f.read()[:30]
```

**Challenge:** Using the file `school_prompt.txt`, assign the third word of every
line to a list called `three`.
```python
three = []
with open("school_prompt.txt") as f:
    for line in f.readlines():
        three.append(line.split(" ")[2])
```

**Challenge:** Create a list called `emotions` that contains the first word of
every line in `emotion_words.txt`.
```python
emotions = []
with open("emotion_words.txt") as f:
    for line in f.readlines():
        emotions.append(line.split(" ")[0])
```

Assign the first 33 characters from the textfile, `travel_plans.txt` to the
variable `first_chars`.
```python
with open("travel_plans.txt") as f:
    first_chars = f.read()[:33]
```

**Challenge:** Using the file `school_prompt.txt`, if the character ‘p’ is
in a word, then add the word to a list called `p_words`.
```python
p_words = []
with open("school_prompt.txt") as f:
    for line in f.readlines():
        for word in line.rstrip().split(" "):
            if "p" in word:
                p_words.append(word)
```


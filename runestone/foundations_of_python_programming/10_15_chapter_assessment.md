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

Read in the contents of the file `SP500.txt` which has monthly data for 2016
and 2017 about the S&P 500 closing prices as well as some other financial
indicators, including the “Long Term Interest Rate”, which is interest rate
paid on 10-year U.S. government bonds.

Write a program that computes the average closing price (the second column,
labeled SP500) and the highest long-term interest rate. Both should be computed
only for the period from June 2016 through May 2017. Save the results in the
variables `mean_SP` and `max_interest`.
```python
i = t = max_interest = 0
with open("SP500.txt") as f:
    for line in f.read().splitlines()[1:]:
        col = line.split(",")
        month, _, year = col[0].split("/")
        if (
            (int(month) >= 6 and year == "2016") or
            (int(month) <= 5 and year == "2017")
        ):
            i += 1
            t += float(col[1])
            if float(col[5]) > max_interest:
                max_interest = float(col[5])
mean_SP = t / i
```

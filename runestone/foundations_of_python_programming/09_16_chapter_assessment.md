# 9.16. Chapter Assessment - List Methods

Write code to add ‘horseback riding’ to the third position (i.e., right before
volleyball) in the list `sports`.
```python
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, "horseback riding")
```

Write code to take ‘London’ out of the list `trav_dest`.
```python
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove("London")
```

Write code to add ‘Guadalajara’ to the end of the list `trav_dest` using a list method.
```python
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append("Guadalajara")
```

## 9.16.2 Chapter Assessment - Split and Join

Write code to find the position of the string “Tony” in the list `awards` and
save that information in the variable `pos`.
```python
awards = ['Emmy', 'Tony', 'Academy', 'Grammy']
pos = awards.index("Tony")
```
## 9.16.3 Chapter Assessment - For Loop Mechanics

Currently there is a string called `str1`. Write code to create a list called
`chars` which should contain the characters from `str1`. Each character in
`str1` should be its own element in the list `chars`.
```python
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
# chars = list(str1)
chars = []
for c in str1:
    chars.append(c)
```

## 9.16.4 Chapter Assessment - Accumulator Pattern

For each character in the string saved in `ael`, append that character to a
list that should be saved in a variable `app`.
```python
ael = "python!"
app = []
for c in ael:
    app.append(c)
```

For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past
tense). Save these past tense words to a list called `past_wrds`.
```python
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = [w+"ed" for w in wrds]
```

Write code to create a **list of word lengths** for the words in `original_str`
using the accumulation pattern and assign the answer to a variable `num_words_list`.
(You should use the len function).
```python
original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = [len(w) for w in original_str.split(" ")]
```

Create an empty string and assign it to the variable `lett`. Then using range,
write code such that when your code is run, `lett` has 7 b’s ("bbbbbbb").
```python
# # lett = "b"*7
# lett = "".join("b" for _ in range(7))
lett = ""
for _ in range(7):
    lett += "b"
```
## 9.16.5 Chapter Assessment - Problem Solving

Below are a set of scores that students have received in the past semester.
Write code to determine how many are 90 or above and assign that result to the
value `a_scores`.
```python
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = sum(1 for x in scores.split(" ") if int(x) >= 90)
```

Write code that uses the string stored in `org` and creates an acronym which is
assigned to the variable `acro`. Only the first letter of each word should be used,
each letter in the acronym should be a capital letter, and there should be nothing
to separate the letters of the acronym. Words that should not be included in the
acronym are stored in the list `stopwords`. For example, if `org` was assigned the
string “hello to world” then the resulting acronym should be “HW”.
```python
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = "".join(c[0].upper() for c in org.split(" ") if c not in stopwords)
```

Write code that uses the string stored in `sent` and creates an acronym which is
assigned to the variable `acro`. The first two letters of each word should be used,
each letter in the acronym should be a capital letter, and each element of the
acronym should be separated by a “. ” (dot and space). Words that should not be
included in the acronym are stored in the list `stopwords`. For example, if `sent`
was assigned the string “height and ewok wonder” then the resulting acronym should
be “HE. EW. WO”.
```python
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ". ".join(str(c[:2]).upper() for c in sent.split(" ") if c not in stopwords)
```

A palindrome is a phrase that, if reversed, would read the exact same. Write code
that checks if `p_phrase` is a palindrome by reversing it and then checking if the
reversed version is equal to the original. Assign the reversed version of `p_phrase`
to the variable `r_phrase` so that we can check your work.
```python
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
```

Provided is a list of data about a store’s inventory where each item in the list
represents the name of an item, how much is in stock, and how much it costs. Print
out each item in the list with the same formatting, using the .format method (not
string concatenation). For example, the first print statment should read
`The store has 12 shoes, each for 29.99 USD`.
```python
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for line in inventory:
    item, stock, price = line.split(", ")
    print("The store has {} {}, each for {} USD.".format(stock, item, price))
```

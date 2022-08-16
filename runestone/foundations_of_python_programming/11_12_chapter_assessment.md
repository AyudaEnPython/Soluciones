# 11.12. Chapter Assessment

## 11.12.1. Assesment - Dictionaries

At the halfway point during the Rio Olympics, the United States had 70 medals,
Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and
Germany had 17 medals. Create a dictionary assigned to the variable
`medal_count` with the country names as the keys and the number of medals the
country had as each key’s value.
```python
medal_count = {
    "United States": 70,
    "Great Britain": 38,
    "China": 45,
    "Russia": 30,
    "Germany": 17,
}
```

Given the dictionary `swimmers`, add an additional key-value pair to the dictionary
with `"Phelps"` as the key and the integer `23` as the value. Do not rewrite the
entire dictionary.
```python
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers["Phelps"] = 23
```

Add the string “hockey” as a key to the dictionary `sports_periods` and assign it
the value of 3. Do not rewrite the entire dictionary.
```python
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"] = 3
```

The dictionary `golds` contains information about how many gold medals each country
won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update `golds` to
reflect this information.
```python
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] += 2 
```

Create a list of the countries that are in the dictionary `golds`, and assign that
list to the variable name `countries`. Do not hard code this.
```python
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds)
```

Provided is the dictionary, `medal_count`, which lists countries and their respective
medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics,
assign the medal count value for `"Belarus"` to the variable `belarus`. Do not hardcode
this.
```python
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count["Belarus"]
```

The dictionary `total_golds` contains the total number of gold medals that countries
have won over the course of history. Use dictionary mechanics to find the number
of golds Chile has won, and assign that number to the variable name `chile_golds`.
Do not hard code this!
```python
total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds["Chile"]
```

Provided is a dictionary called `US_medals` which has the first 70 metals that the
United States has won in 2016, and in which category they have won it in. Using
dictionary mechanics, assign the value of the key `"Fencing"` to a variable
`fencing_value`. Remember, do not hard code this.
```python
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals["Fencing"]
```

## 11.12.2. Assessment - Dictionary Accumulation

The dictionary `Junior` shows a schedule for a junior year semester. The key is
the course name and the value is the number of credits. Find the total number
of credits taken this semester and assign it to the variable `credits`. Do not
hardcode this – use dictionary accumulation!
```python
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = sum(Junior[k] for k in Junior)
```

Create a dictionary, `freq`, that displays each character in string `str1` as the
key and its frequency as the value.
```python
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for letter in str1:
    if letter not in freq:
        freq[letter] = 0
    freq[letter] += 1
```

Provided is a string saved to the variable name `s1`. Create a dictionary named
`counts` that contains each letter in `s1` and the number of times it occurs.
```python
s1 = "hello"
counts = {}
for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1
```

Create a dictionary, `freq_words`, that contains each word in string `str1` as the
key and its frequency as the value.
```python
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
for word in str1.split(" "):
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
```

Create a dictionary called `wrd_d` from the string `sent`, so that the key is a word
and the value is how many times you have seen that word.
```python
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
for word in sent.split(" "):
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
```

Create the dictionary `characters` that shows each character from the string `sally`
and its frequency. Then, find the most frequent letter based on the dictionary.
Assign this letter to the variable `best_char`.
```python
sally = "sally sells sea shells by the sea shore"
characters = {}
for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] += 1
best_char = max(characters, key= lambda x: characters[x])
```

Find the least frequent letter. Create the dictionary `characters` that shows each
character from string `sally` and its frequency. Then, find the least frequent
letter in the string and assign the letter to the variable `worst_char`.
```python
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for letter in sally:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] += 1
worst_char = min(characters, key= lambda x: characters[x])
```

Create a dictionary named `letter_counts` that contains each letter and the number
of times it occurs in `string1`. **Challenge**: Letters should not be counted separately
as upper-case and lower-case. Intead, all of them should be counted as lower-case.
```python
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}
for letter in string1:
    letter = letter.lower()
    if letter not in letter_counts:
        letter_counts[letter] = 0
    letter_counts[letter] += 1
```

Create a dictionary called `low_d` that keeps track of all the characters in the
string `p` and notes how many times each character was seen. Make sure that there
are no repeats of characters as keys, such that “T” and “t” are both seen as
a “t” for example.
```python
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for letter in p:
    letter = letter.lower()
    if letter not in low_d:
        low_d[letter] = 0
    low_d[letter] += 1
```

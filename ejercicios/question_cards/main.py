"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

data = [
    {
        "Question": "aaaaaa.\n",
        "Correct": "True",
        "A": "",
        "B": "False",
        "C": "True",
        "D": "",
    },
    {
        "Question": "bbbb.\n",
        "Correct": "a",
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
    },
]


def remove_empty_options(card):
    return {k: v for k, v in card.items() if v}


def remove_newline(card, key="Question"):
    return {k: v.strip() if k == key else v for k, v in card.items()}


def answer_option(card, key="Correct"):
    for k, v in card.items():
        if v == card[key] and k != key:
            card[key] = k
    return card


print(data)
print("----")
for card in data:
    print(answer_option(remove_newline(remove_empty_options(card))))

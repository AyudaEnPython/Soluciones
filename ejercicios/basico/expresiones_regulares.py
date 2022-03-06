"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una expresión regular para cada caso:
- Todos los usuarios que sigan el patron: User_mentions: 9
- Encuentre los numeros de likes: 5
- Que permita encontrar el numero de retweets: 4

NOTE: El enunciado no es especifico.
"""
import re

s = (
    "Unfortuantely one of those moments wasn't a giant squid monster. "
    "User_mentions: 2, likes: 9, number of retweets: 7"
)

users = re.compile(r"User_mentions: (\d+)")
likes = re.compile(r"likes: (\d+)")
retweets = re.compile(r"number of retweets: (\d+)")

for regex in [users, likes, retweets]:
    print(regex.findall(s))

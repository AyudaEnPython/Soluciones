"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

entered_number = input('Your Number?: ')

pattern = '|'.join([str(f"{number}$") for number in numbers])

match = re.match(f'{pattern}', entered_number, flags=0)

if match:
    print('The number exists!')
else:
    print('Holly crap!! This number does not exist!')
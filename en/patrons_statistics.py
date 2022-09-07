"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)

data = []
for month in MONTHS:
    patrons = int(input(f"Enter number of patrons for {month}: "))
    data.append(patrons)

most = max(data)
least = min(data)
average = sum(data) / len(data)

print(f"{MONTHS[data.index(most)]} had the most patrons.")
print(f"{MONTHS[data.index(least)]} had the least patrons.")
print(f"Average monthly visitors are {average:.2f}.")

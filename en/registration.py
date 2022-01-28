"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""

names = []
print("Simple Registration Program")
print("===========================\n")

while True:
    name = input("Enter a name: ")
    if name == "done":
        break
    if name == "":
        print("Invalid name! Try again.")
        continue
    if name not in names:
        names.append(name)
    else:
        print(f"{name} already exists. Try again.")

print("List of registered names:")
print(names)
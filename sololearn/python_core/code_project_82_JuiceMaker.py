"""
Juice Maker
===========

You are given a Juice class, which has name and capacity properties.
You need to complete the code to enable and adding of two Juice
objects, resulting in a new Juice object with the combined capacity and
names of the two juices being added.

For example, if you add an Orange juice with 1.0 capacity and an Apple
juice with 2.5 capacity, the resulting juice should have:
name: Orange&Apple
capacity: 3.5

The names have been combined using an & symbol.

NOTE: Use the __add__ method to define a custom behavior for the +
operator and return the resulting object.
"""


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        return Juice(
            self.name + "&" + other.name, self.capacity + other.capacity
        )
    
    def __str__(self):
        return f"{self.name} ({str(self.capacity)}L)"


a = Juice("Orange", 1.0)
b = Juice("Apple", 2.5)

result = a + b
print(result)
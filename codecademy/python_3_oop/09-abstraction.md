# OOP Pillar: Abstraction

When a program starts to get big, classes might start to share functionality or we may lose sight of the purpose of a class’s inheritance structure. In order to alleviate issues like this, we can use the concept of abstraction.

Abstraction helps with the design of code by defining necessary behaviors to be implemented within a class structure. By doing so, abstraction also helps avoid leaving out or overlapping class functionality as class hierarchies get larger.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
    self.name = name

  @abstractmethod
  def make_noise(self):
    pass

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"
``` 

Above we have `Cat` and `Dog` classes that inherit from `Animal`. The `Animal` class now inherits from an imported class `ABC`, which stands for Abstract Base Class.

This is the first step to making `Animal` an abstract class that cannot be instantiated. The second step is using the imported decorator `@abstractmethod` on the empty method `.make_noise()`.

The below line of code would throw an error.

```python
an_animal = Animal("Scruffy")

# TypeError: Can't instantiate abstract class Animal with abstract method make_noise
```

The abstraction process defines what an `Animal` is but does not allow the creation of one. The `.__init__()` method still requires a name, since we feel all animals deserve a name.

The `.make_noise()` method exists since all animals make some form of noise, but the method is not implemented since each animal makes a different noise. Each subclass of Animal is now required to define their own `.make_noise()` method or an error will occur.

These are some of the ways abstraction supports the design of an organized class structure.

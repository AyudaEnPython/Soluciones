# The @property Decorator

Learn about the most pythonic way of using getters, setters, and deleters!

## Introduction

In this article, we’ll explore the @property decorator - a more pythonic way to use getters and setters in our object-oriented programs! Before we dive in, let’s briefly review the concept of getters and setters.

Let’s recall that getters and setters are useful tools for achieving encapsulation (a way to prevent data from direct modification). We can define a private attribute and then use getters and setters to expose a public means of reading and modifying a class attribute value. Further, getters and setter methods allow us to create complex behavior such as limiting access under certain conditions or imposing restrictions on allowable ranges of values for an attribute.

Let’s start by looking at an example class called `Box` with one attribute called `weight`. In this case, `weight` will be a private attribute with a getter and a setter (`getWeight()` and `setWeight()`).

```python
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
```

Notice two things:

- We want to follow best practices by denoting weight as a private attribute using `__` (dunder) notation. This, however, does not make an attribute private, and we can still manipulate it directly.

- We are also posing some restrictions on our setter so that the weight of an instance of the `Box` class can only be set to values greater than zero. We can see this if we try to manipulate an instance:
    ```python
    box = Box(10)

    box.setWeight(-5) 
    print(box.getWeight())

    box.setWeight(5)
    print(box.getWeight())
    ```

  That our box weight was unchanged on the first call:
  ```
  10
  5
  ```

Notice that we need to call the methods instead of directly interacting with the weight attribute. What if we could have the best of both worlds? That is, a way to directly interact with the weight attribute but still benefit from the complex behavior of methods such as the weight restriction. This is where the built-in function property() comes in.

## The built-in property() function

The Python built-in `property(` function accepts four optional arguments: `fget`, `fset`, `fdel`, and `doc`. The first three represent getter, setter, and deleter methods, respectively, and the last one is a docstring for the attribute.

Let’s take a look at the advantages by refactoring our `Box` class:
```python
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
```

Notice we have added one additional method to our class called `delWeight()` to serve as a deleter for the property. While it is not strictly required, we will add it to show the full potential of the `property()` function. We then call the `property()` function and pass the getter, setter, and deleter in as arguments. This will immediately allow us to use the following syntax for our class:

```python
box = Box(10)

print(box.weight) #this calls .getWeight()

box.weight = 5 #this called .setWeight()

del box.weight #this calls .delWeight()

box.weight = -5 #box.__weight is unchanged 
```

With this change, our program gains some immediate benefits:

- We can now use the `weight` attribute as if it was public. We no longer have to call the setters, getters, and deleter methods directly and thus giving our program a simpler syntax.
- Even though we no longer call the methods directly, we still can maintain constraints such as the weight limit in `setWeight()`. It’s the best of both worlds!
- If we had a huge codebase that used our methods multiple times in multiple places, a single change to the method name would seriously mess up our program since we would have to change it everywhere! We no longer have this issue using the `property()` method since we never call it directly.

While this is a big advantage for our programs to be more “pythonic”, we can go even further by using the decorator pattern to replace the need to call the `property()` function altogether.

## @property Decorator

The most pythonic way to define getters, setters, and deleters is by using the `@property` decorator. This decorator is syntactic sugar for using the `property()` function and helps our code look much cleaner. Let’s take a look:

```python
class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight


 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter
 def weight(self):
   del self.__weight
```

Lets break this down:

- First, we have renamed all of our methods to simply be `weight()`.
- Then we denoted our getter with a `@property`. This marks the property to be used as a prefix for decorating the setter and deleter methods.
- Lastly, we use `@weight.setter` and `@weight.deleter` to define our setter and deleter methods, respectively.

This is the equivalent of doing:

```python
weight = property(getWeight, setWeight, delWeight,  "Docstring for the 'weight' property")
```

And thus giving us the same synthactical advantage as before:

```python
box = Box(10)

box.weight = 5

del box.weight
```

## Wrap up


To summarize, we learned:

- The limitations of using regular setter and getter methods.
- How to use the `property()` function to create cleaner getters, setters, and deleters.
- The `@property` decorator is the most “pythonic” way to use the `property()` function.

When using the decorator, remember three rules:

- All three methods must use the same member name (ex. `weight`).
- The first method must be the getter and is identified using `@property`.
- The decorators for the setter and deleter are defined by the name of the method `@property` is used with.

Keep the `@property` decorator in mind when approaching any object-oriented program! It will save time and keep code cleaner and more maintainable.

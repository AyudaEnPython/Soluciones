# Example solution:
#
# from abc import ABC, abstractmethod
# 
# class AbstractEmployee(ABC):
#   new_id = 1
#   def __init__(self):
#     self.id = AbstractEmployee.new_id
#     AbstractEmployee.new_id += 1
# 
#   @abstractmethod
#   def say_id(self):
#     pass
# 
# # Write your code below
# class Employee(AbstractEmployee):
#     def say_id(self):
#       print("My id is {}".format(self.id))
# 
# e1 = Employee()

from abc import ABC, abstractmethod


class AbstractEmployee(ABC):

    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        ...


class Employee(AbstractEmployee):

    def say_id(self):
        print(f"My id is {self.id}.")


e1 = Employee()
e1.say_id()

# Example solution
#
# class Employee():
#   new_id = 1
#   def __init__(self):
#     self.id = Employee.new_id
#     Employee.new_id += 1
# 
#   def say_id(self):
#     print("My id is {}.".format(self.id))
# 
# class Admin(Employee):
#   def say_id(self):
#     super().say_id()
#     print("I am an admin.")
# 
# class Manager(Admin):
#   def say_id(self):
#     print("I am in charge!")
#     super().say_id()
# 
# # Write your code below
# meeting = [Employee(), Admin(), Manager()]
# for member in meeting:
#   member.say_id()


class Employee:

    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}.")


class Admin(Employee):

    def say_id(self):
        super().say_id()
        print("I am an admin.")


class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge!")


meeting = [Employee(), Admin(), Manager()]
for member in meeting:
    member.say_id()

# Example solution:
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
# # Write your code below
# class Admin(Employee):
#   pass
# 
# e1 = Employee()
# e2 = Employee()
# e3 = Admin()
# e3.say_id()


class Employee:

    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}.")


class Admin(Employee):
    ...


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

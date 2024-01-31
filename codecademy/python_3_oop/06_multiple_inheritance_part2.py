# Example solution

# class Employee():
#   new_id = 1
#   def __init__(self):
#     self.id = Employee.new_id
#     Employee.new_id += 1

#   def say_id(self):
#     print("My id is {}.".format(self.id))

# class User:
#   def __init__(self, username, role="Customer"):
#     self.username = username
#     self.role = role

#   def say_user_info(self):
#     print("My username is {}".format(self.username))
#     print("My role is {}".format(self.role))

# # Write your code below
# class Admin(Employee, User):
#   def __init__(self):
#     super().__init__()
#     User.__init__(self, self.id, "Admin")

#   def say_id(self):
#     super().say_id()
#     print("I am an admin.")

# e1 = Employee()
# e2 = Employee()
# e3 = Admin()
# e3.say_user_info()


class Employee:

    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}.")


class User:

    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"My username is {self.username}")
        print(f"My role is {self.role}")


class Admin(Employee, User):

    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print("I am an admin.")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()

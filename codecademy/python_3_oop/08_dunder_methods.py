# Example solution
#
# class Employee():
#   new_id = 1
#   def __init__(self):
#     self.id = Employee.new_id
#     Employee.new_id += 1
# 
# class Meeting:
#   def __init__(self):
#     self.attendees = []
#   
#   def __add__(self, employee):
#     print("ID {} added.".format(employee.id))
#     self.attendees.append(employee)
# 
#   # Write your code
#   def __len__(self):
#     return len(self.attendees)
#     
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# m1 = Meeting()
# m1 + e1
# m1 + e2
# m1 + e3
# print(len(m1))

class Employee:

    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1


class Meeting:

    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print(f"ID {employee.id} added.")
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

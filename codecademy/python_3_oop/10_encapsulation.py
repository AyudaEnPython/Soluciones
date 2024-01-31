# Example solution
#
# class Employee():
#     def __init__(self):
#         self.id = None
#         # Write your code below
#         self._id = None
#         self.__id = None
# 
# e = Employee()
# print(dir(e))


class Employee:

    def __init__(self):
        self.id = None
        self._id = None
        self.__id = None


e = Employee()
print(dir(e))

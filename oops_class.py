# class Employee:
#     def emp_det(emp):
#         emp.name="rohit"
#         emp.country="USA"
# emp1= Employee()
# emp1.emp_det()
# emp1.name=""
#
# print(emp1.name)
# print(emp1.country)

# Problem statement
# What will be the output of following code?

class Student:
    name = 'Parikh'
    def store_details(self):
        self.age = 60

    def print_age(self):
        print(self.age)
s = Student()

s.store_details()
s1 = Student()
s.print_age()
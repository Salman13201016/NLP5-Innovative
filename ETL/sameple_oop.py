
import datetime
from pprint import pprint
class Student:
    def __init__(self,b,a): #constructor = #initializer
        print("this is a constructor")
        self.name = a
        self.email = b
        self.joined= datetime.datetime.now()


student1 = Student(x='salman',y='xyz')
print(student1.name)
student2 = Student('kanita','xyz3')
student3 = Student('farha','xyz34')
# print(student1.name)
# print(student2.name)
# print(student3.name)
print(student1.__dict__)
pprint(student1.__dict__)

# print(student2)


# constructor is the initialization function
# the self parameter is a reference to the current instance of the class and is used
# to access variables that belong to the class
# ============++++++++++++=============
# class Student:
#     name="Brother"
#     marks=345
#     gpa=3.90
#     semester=2
#     def __init__(self,fullname):  # self is always the first parameter, any other name can also be written for self like abc,first etc but self is good programming
#         print(self)
#         print("Adding new student to the class...")
# s1=Student()  # if here ()  are not added to the class name, then the constructor is not called
# print(s1)
# print(s1.name)
# print(s1.marks)
# ++++++++++++===========+++++++++++++  
# class Car:
#     color="Blue"
#     model="Mercedes"
#     def __init__(self):  # default constructor 
#         print("Default constructor is called")
#     def __init__(self,color):  # parametarized constructor
#         self.color=color
#         print("New car is being manufacturing .... ")
# c1=Car("Red")
# print(c1.color,"\t",c1.model)
# c2=Car("White")
# print(c2.color,"\t",c2.model)
###############  class and object(instance) attributes
# class Student:
#     college_name="Islamia college peshawar" # class attribute
#     name="Anonymous"
#     def __init__(self,name,marks):
#         self.name=name  # instance attribute
#         self.marks=marks
#         print("Object successfully created!")
# print(Student.college_name)
# s1=Student("Ahmad","899")
# print(s1.college_name,"\t",s1.name,"\t",s1.marks,"\n")
############### Method in classes  
# class Student:
#     college_name="Islamia college peshawar" # class attribute
#     name="Anonymous"
#     def __init__(self,name,marks):
#         self.name=name  # instance attribute
#         self.marks=marks
#         print("Object successfully created!")
#     def welcome(self):
#         print("\nYour are all welcome to this amazing and fascinating school, all the best for your journey\n")
#     def get_marks(self):
#         return self.marks
# s1=Student("Brother",5634)
# s1.welcome()
# print(s1.get_marks())
######## practice questions  01
# class Student:
#     def __init__(self):
#         self.name=input("Enter your name : ")
#         self.m1=input("Enter marks of first subject : ")
#         self.m2=input("Enter marks of second subject : ")
#         self.m3=input("Enter marks of third subject : ")
#         print("Your object is created successfully\n")
#     def find_average(self):
#         return (int(self.m1)+int(self.m2)+int(self.m3))/3
# s1=Student()
# print("The average of your marks is ",s1.find_average())
##########################  Static method
# static method are those mehtods which don't use self parameter
# decorator allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
class Student:
    @staticmethod  # decorator\
    def hello(): # now it don't need any self parameter
        print("Hello brothers and sisters, how are you")
s1=Student()
s1.hello()
####################### Abstraction and encapsulation
# Abstraction : hiding the implementation details of a class and only showing the essential features to the user
# Encapsulation : wrapping data and functions into a single unit (object)







# study getter and setter decorators

# del keyword : used to delete object properties or object itself
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Muhammad Atif")
# print(s1.name)
# print(s1)
# del s1
# print(s1.name)  # it will give us error as object is deleted 
#########################################
# private attributes and methods 
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass  #  __ is used for making something private
#     def acc_pass(self):
#         print("Your account ",self.acc_no,"has password : ",self.__acc_pass)    
# acc1=Account("4253g3445","5t#$*vE4")
# print(acc1.acc_no)
# # print(acc1.acc_pass)   # as it is private data, so it will give us error
# print(acc1.acc_pass())
######################################### Inheritance
# class Car:
#     color="Black"
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car parked...")
# class ToyataCar(Car):
#     def __init__(self,name):
#         self.name=name
# car1=ToyataCar("Fortuner")
# car2=ToyataCar("Prius")
# print(car1.name)
# print(car1.start())
# print(car1.color)
################# multiple inheritance
# class A:
#     vara="You are inside A class"
# class B:
#     varb="You are inside B class"
# class C(A,B):
#     varc="You are inside C class"
# c1=C()
# print("\n",c1.vara,"\t",c1.varb,"\t",c1.varc,"\n")
#################  Super method : super() method is used to access methods of the parent class
# class Car:
#     def __init__(self,type):
#         self.type=type
#     color="Black"
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car parked...")
# class ToyataCar(Car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)  # for passing type value to the parent constructor
# car1=ToyataCar("Fortuner","Electric")
#################   class methods : a class method is bound to the class and recieve the class as an implicit first argument
class Person:
    name="Muhammad Atif"
    
    def change_name(self,name):  # changing object name
        self.name=name   #  here self refers to the instance 
    # 01 way    
    def change_class_attribute(self,name):  # function for changing class attribute value
        Person.name=name    
    # 02 way
    def change(self,name):
        self.__class__.name=name
    # 03   through class method
    @classmethod
    def changeName(cls,name):  # here cls refers to class 
        cls.name=name
p1=Person()
print(p1.name)
p1.change_name("No one")
print(p1.name) 
print(Person.name)
p1.change_class_attribute("Some one is here")
print(Person.name)
p1.change("why not")
print(Person.name)

# @property decorator : we use @property decorator on any method in the class to use the method as a property
print("__+_+_+_+    @Property decorator    +_+_+_+__")
class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
    
    @property
    def percentage(self):
        return str((self.math+self.phy+self.chem)/3)+"%"

stu1=Student(78,98,56)
print(stu1.percentage)

stu1.chem=77

print(stu1.percentage)


####  POLYMORPHISM  ###
# implicit operator overloading
print(234+456)
print("Hello "+"World")  # cancatenate
print([43,45,56]+[23,12,59])  # merge

# practice code
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showdata(self):
        print(self.real,"+",self.img,"i")

    def add(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)

    def __add__(self,num2):   # dender function( when __ is used) ---> operator overloading
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)

num1=Complex(5,3)
num1.showdata()

num2=Complex(8,7)
num2.showdata()

num3=num1.add(num2)
num3.showdata()

num4=num1+num2
num4.showdata()


























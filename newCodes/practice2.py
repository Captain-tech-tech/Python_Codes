

# import math as m
# import math
# from math import sqrt

# Floats are not always exact, so compare them with math.isclose instead of ==
# import math
# print(0.1 + 0.2 == 0.3)
# print(math.isclose(0.1 + 0.2, 0.3))

# print(m.sqrt(25))
# print(m.pi)
# print(m.factorial(5))




# import random
# print(random.randint(1,10))

# random.random()	a float from 0 up to (not including) 1	0.5714
# random.randint(a, b)	an int from a to b, both included	randint(1, 6) → 4   # it returns a whole number
# random.uniform(a, b)	a float between a and b	uniform(1, 5) → 3.27  # it returns a floating number
# random.choice(seq)	one item from a sequence	'Sadia'
# random.sample(seq, k)	a new list of k different items	['Zara', 'Ali']
# random.choices(seq, k=n)	a new list of n items, repeats allowed	['Ali', 'Ali', 'Omar']
# print(random.choices(list,k = 11))
# random.shuffle(lst)	nothing; it mixes the list itself	None
# random.seed(n)	nothing; it fixes the starting point	None

# random.seed(42)
# print(random.randint(1, 100))  # Will ALWAYS print 82
# print(random.randint(1, 100))  # Will ALWAYS print 15





# import os
# print(os.getcwd())  
# print(os.listdir())   # files in the current directory

# import sys
# print(sys.version)




# from datetime import date
# print(date.today())

# import datetime
# print(datetime.date.today())




# Module          = One Python File
# Package         = Collection of Modules
# Import          = Use Code from Another Module
# Built-in Module = Already Comes with Python
#include        = Copy Header File Contents (C/C++)



# import university.faculty.teachers#package(package, it has __init__.py file), subpackage(faculty, this subpakage has its own __init__.py file), module(teachers)
# university.faculty.teachers.display_teacher()

# from university.faculty import teachers
# teachers.display_teacher()

# from university.faculty.teachers import display_teacher
# display_teacher()

# import university.faculty.teachers as t
# t.display_teacher()


# from .teachers import display_teacher
# display_teacher()
# The dot (.) means:
# Current Package
# Similarly,
# from ..students.records import show_record
# means:
# Go one level up,
# then enter students package,
# then import records module.

# Package
#    └── Sub-package
#           └── Module
#                  └── Function/Class




# "r"	Read only
# "w"	Write (overwrite)
# "a"	Append
# "x"	Create new file
# "r+"	Read and write
# "w+"	Write and read
# "a+"	Append and read


# file = open("sample.txt", "r")  # FileNotFoundError occurs if file is not present
# f = file.read()
# c = file.read(3)#here c stores and prints an empty string b/c internal file pointer moves to the end in previous code
# print(f)
# print("\n\n",c)
# file.close()


# file = open("sample.txt",'r')
# c = file.read(10)
# print(c)
# file.close()


# file = open("sample.txt","r")
# l1 = file.readline()
# print(l1)
# l2 = file.readline()
# print(l2)


# file = open("sample.txt", 'r')
# lines = file.readlines()
# print(lines)


# f = open("new.txt", "w")
# f.write("Hello welcome home")
# f.write("I am nothing")
# f.close()


# f = open("new.txt", "a")
# f.write("Why are you here, and what are you doing here")
# f.close()



# file = open("newfile.txt", "x")  # just to create new file
# file.close()


# with open("sample.txt","r") as f:
#     print(f.read())


# Absolute path
# Full location from root directory, works regardless of current folder, usually longer, Useful when exact location is known
# file = open("/home/admin/data.txt", "r")

# Relative path
# Relative to current working directory, shorter and more portable, commonly used in projects, easier to move projects.
# file = open("data.txt", "r")




# it combines folder and file names safely
# import os
# path = os.path.join("data", "students.txt")
# print(path)

# path = os.path.join("data", "CS", "Semester3", "students.txt")
# print(path)

# os.path.exists(filename)  # is there such a file exists or not





# from pathlib import Path
# # Creates a file path by joining the folder and file name.
# file_path = Path("data") / "students.txt"
# print(file_path)



# f = open("sample.txt","r")
# for i in f:
#     print(i,end="")
# print(repr(f))  # repr tells about file mode etc



# strip() removes spaces and '\n' from both ends
# with open("sample.txt",'r') as f:
#     for i in f:
#         print(repr(i))  # repr shows the hidden '\n'
#         print(i.strip())




# print('a-b-c'.split('-'))

# lines = []
# with open("sample.txt", 'r') as f:
#     lines = f.read().split('\n')
# print(lines)





# try:
#     num = int(input("Enter number: "))
#     result = 100 / num
#     print(result)
# except ValueError:
#     print("Invalid input! Please enter an integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")



# try:
#     print(unknown_variable)
# except ValueError:
#     print("Invalid input!")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except:
#     print("couldn't find the error")




# try:
#     i = int(input("Enter a number :"))
#     m = 34/i
# except Exception as e:
#     print(type(e).__name__)

# print("Continue")




# def get_percentage(obtained, total):
#     return obtained/total*100

# try:
#     get_percentage(34,0)
# except Exception as e:
#     print(type(e).__name__)



# while True:
#     try:
#         age = int(input("Enter your age: "))
#         break
#     except ValueError:
#         print("Please enter digits only. Try again.")

# print("Your age is", age)





# fruits = ["apple", "banana", "mango"]

# try:
#     index = int(input("Enter index (0-2): "))
#     print("Fruit:", fruits[index])
# except IndexError:
#     print("Index out of range.")



# dict = {
#     "pen":45,
#     "pointer":56,
#     "notebook":43,
#     "book":89
# }

# try:
#     n = input("Enter index number :")
#     print(dict[n])
# except IndexError:
#     print("Out of range index entered")
# except KeyError:
#     print("Invalid key entered")




# # important --------------------
# data = ["10", "25", "abc", "40", "4.5", "7"]
# numbers = []

# for item in data:
#     try:
#         numbers.append(int(item))
#     except ValueError:
#         print("Skipping invalid value:", item)

# print("Valid numbers:", numbers)
# print("Sum:", sum(numbers))






# raise statement is used to generate an exception intentionally
# age = int(input("Enter age: "))
# if age < 0:
#     raise ValueError("Age cannot be negative")
# print("Age =", age)


# marks = int(input("Enter marks: "))
# if marks < 0 or marks > 100:
#     raise ValueError("Marks must be between 0 and 100")
# print("Valid Marks")


# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Age =", age)
# except ValueError as e:
#     print("Error:", e)
# finally:
#     print("Thank you for using the program.")


# try:
#     n = int(input("Enter a number:"))
#     if(n<0 or n>100):
#         raise ValueError("Invalid value is entered, out of range")
# except ValueError as e:
#     print(e)
# else:
#     print("No error occured")
# finally:
#     print("Thanks for using our program, we are very thankful to you")



# class Student:
#     ...
# s1 = Student()
# print(type(s1))
# print(s1)


# class Student:
#     pass
# s1 = Student()
# s2 = Student()
# s3 = s1          # s3 is NOT a new object, it points to s1
# print(s1 == s2)
# print(s1 == s3)
# print(isinstance(s1, Student))






# class Student:
#     def __init__(self, parameter,name):
#         self.parameter = parameter
#         self.name = name
#     def show(self):
#         print(self.parameter)
#         print(self.name)

# s = Student(34)
# s.show()
# print(s.parameter)




# class Phone:
#     def __init__(self, brand):
#         print("A new phone is being created...")
#         self.brand = brand
# p1 = Phone("Samsung")
# p2 = Phone("Apple")
# print(p1.brand)
# print(p2.brand)




# class Student:
#     def __init__(self, name, city="Lahore"):
#         self.name = name
#         self.city = city
# s1 = Student("Ali")
# s2 = Student("Sara", "Karachi")
# print(s1.name, "-", s1.city)
# print(s2.name, "-", s2.city)



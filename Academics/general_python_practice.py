print(2/4)
print(2//4)  # floor 
print(2//4.0)
print(1%2)
print(1/2.0)
print(type(1/2))




x = 3.4  # ceil function
if x == int(x):
    x = int(x)
else :
    x = int(x) + 1
print(x)


print((("ab"+'cd')*3)+"WHY"+"HELLO")
print("ab" + "cd")
print('a-' * 3)


print(True or False and False or False)   # and has a higher precendence
print((True or False) and (False or False))

# min, max, pow
___h = 3556
_hello = 34
print(_hello)


is_passed = True
print(type(is_passed))


# taking input from the user




name = "Ali"
age = 20

print(f"My name is {name} and I am {age} years old.")


print(2 ** 3)

# **=  ,  //=



name = None
# Here, name does not contain a person's name. It currently has no value.

if name is None:
    print("No name was provided")


# work on in, not in, is and is not operators

# in / not in → membership: “Is this value present inside this collection?”
# The in operator checks whether a value exists inside another object.
nums = [34,57,34,46,34,35,35,34]
print(34 in nums)

n = "python programming"
# print(gramm in n) 
print("gramm" in n)


student = {
    "name": "Ali",
    "age": 20,
    "city": "Peshawar"
}
print("name" in student)   # True
print("Ali" in student)    # False
print("name" in student.keys()) # True
print("Ali" in student.values()) # True




# is / is not → identity: “Are these two variables referring to the exact same object?”

# is does not ask whether two objects have the same value.Are these two variables referring to the 
# exact same object in memory?

a = [1, 2, 3]
b = a  #b = a   doesn't create a new list, both variables refer to the same list object.
print(a is b)  # true
b = [45,45,46]
print(a is b)  # false
# conceptually
#         ┌─────────────┐
# a ─────►│             │
#         │ [1, 2, 3]   │
# b ─────►│             │
#         └─────────────┘

#    == checks equality, is checks identity.


# is not checks whether two variables refer to different objects.
a = [1,2,3]
b = [1,2,3]
print(a is not b)  # true



# None is a special singleton object in Python.
result = None
if result is not None:
    print(result)




value = None
print(value is None)


# value = 2
# print(value is 2)



student = {
    "name": "Ali",
    "age": 20
}
print("name" in student)
print("marks" not in student)



# Logical operators combine multiple conditions.
# Assignment operators update variable values efficiently.
# Identity operators (is, is not) compare object identities (memory locations), not values.
# Membership operators (in, not in) make searching within collections simple and readable.
# Python's is and in operators have no direct equivalents in C/C++, making them unique and widely used features of Python.





# value_if_true if condition else value_if_false
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)




day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")




match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:    #  _ is used for default case
        print("Invalid")


day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

day = "Saturday"

match day:
    case "Saturday" | 1:
        print("Weekend")
    case _:
        print("Weekday")





fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)




for i in range(5):
    print(i)



count = 1
while count <= 5:
    print(count)
    count += 1

# break and continue    



for i in range(3):
    for j in range(2):
        print(i, j)




for ch in "Python":
    print(ch)




# List Comprehension (Compact form of for)
squares = [x*x for x in range(5)]
print(squares)
print("------Equivalent Detailed/shortcut form of above -------")
lst = []
for x in range(5):
    lst.append(x*x)
print(lst)



# Use `enumerate()` when you need both the index and the value while looping through a sequence.
# Important concept : enumerate() returns an enumerate object that produces index-value pairs. 
# More precisely, enumerate() returns an enumerate object, which is an iterator.
colors = ["Red", "Green", "Blue"]
for index, color in enumerate(colors):
    print(index, color)



fruits = ["Apple", "Banana", "Mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print('===== 1 ====')
for i in enumerate(fruits): # i contains the entire tuple produced by enumerate().
    print(i)
for i in enumerate(fruits):
    print(i[0])
for i in enumerate(fruits):
    print(i[1])
print('===== 2 ====')
for fruit in enumerate(fruits):
    print(index, fruit)     # as index above is use, so index value will be printed again and again,
#                           # if it is not define earlier, it will throw an error

c = ["Apple", "Banana", "Mango", "Strawberry"]
for i in range(len(c)):
    print(i, c[i])




# Use `zip()` to iterate over two or more sequences simultaneously, pairing their corresponding elements together.
names = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 95]
for name, mark in zip(names, marks):
    print(name, mark)



student = {
    "name": "Ali",
    "age": 20
}
for key, value in student.items():
    print(key, value)



data = ""
while data != "exit":
    data = input("Enter command: ")





while True:
    choice = input("Enter q to quit: ")
    if choice == "q":
        break




# The `pass` statement is used when you want to leave a block of code empty without causing an error.
for i in range(5):
    if i == 2:
        pass
    print(i)



num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)




n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(fact)




def greet(name):  # name is parameter 
    print("Hello", name) 
greet("Ali")   # 'ALi' is argument




def greet(name): 
    return "Hello " + name 
print(greet("Umer"))





def upp(val:str)->str:
    return val.upper()
print(upp("why are you here"))


def is_positive(num): 
    return num > 0 
print(is_positive(10)) 
print(is_positive(-5))




def total(numbers): 
    return sum(numbers) 
print(total([10, 20, 30]))



def square_list(nums):
    result = []         # creating an empty list
    for n in nums:
        result.append(n * n)
    return result
numbers = [1, 2, 3, 4]
print(square_list(numbers))




def first_item(data): 
    return data[0] 
print(first_item((100, 200, 300)))




def student(): 
    return ("Ali", 21, "CS") 
print(student())




def get_name(student): 
    return student["name"] 
data = {"name": "Ahmed", "age": 20} 
print(get_name(data))




def create_student(): 
    return { "name": "Sara", "age": 22 } 
print(create_student())




def student_info(name, age, cgpa): 
    return f"{name} is {age} years old and has CGPA {cgpa}" 
print(student_info("Ali", 21, 3.7))




def calculate(a, b): 
    return a + b, a - b, a * b 
sum_val, diff_val, prod_val = calculate(10, 5) 
print(sum_val) 
print(diff_val) 
print(prod_val)



# - Functions without `return` automatically return `None`.
def show_message(): 
    print("Python Function") 
result = show_message() 
print(result)




# finding factorial, computing x power n, even or odd checker, thrid largest

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest(10, 25, 15))
print(largest(50, 20, 30))
print(largest(7, 7, 3))





name = "Ali"
def show():
    name = 'Ahmad'
    print(name)
show()
print(name)



name = "atif"
def n():
    # print(name)
    name = "Ali"
    print(name)
n()






count = 10
def increase():
    global count
    count += 1
increase()
print(count)



# Python doesn't allow the same name to be local and global within the same function.
count = 10
def increase():
    count = 20       # local variable
    print("Local:", count)
    # global count
    print(count)





x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print(x)
    inner()
    print(x)
outer()
print(x)





# Python searches variables in the following order:
# LEGB Rule L → E → G → B
# Local → Enclosing → Global → Built-in 
# If Python can't find the name in any of these four scopes, you get a `NameError`.





def power(base, exponent=2):
    return base ** exponent
print(power(5))
print(power(5, 3))



# Non-default parameters must come before default parameters.
# Correct
def func(a, b=10):
    pass
# Incorrect
# def func(a=10, b):
#     pass



# A **lambda function** is a small anonymous function that can have any number of arguments but only one 
# expression. Lambda functions are mainly used for small expressions that produce a value.
# lambda arguments: expression


square = lambda x: x * x
print(square(5))


add = lambda a, b: a + b
print(add(3, 4))


sq = lambda x,y=7,z=5,t=2,l=4: x+y+z+t+l
print(sq(3))



# `map()` applies a function to each element of an iterable (like a list) and returns the transformed values.
# map(function, iterable)


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)
print(numbers)



# Equivalent Code without Lambda
numbers = [1, 2, 3, 4]
def square(x):
    return x * x
squares = list(map(square, numbers))
print(squares)
print(numbers)



n1 = [34,56,23,45,23,35,34]
def square(a):
    return a*a
s = list(map(square, n1))
s











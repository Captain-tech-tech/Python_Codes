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


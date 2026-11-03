# is, is not, in , not in
# value_if_true if condition else value_if_false

# select a portion and shift+""

# time = 6
# match time:
#     case 4 | 5:
#         print("it is used for or opertion in match case statements")
#     case 1:
#         print("Why are you so on time")
#     case _: # default case
#         print("I am always on time")



# # list comprehension
# l1 = [34,56,3,57,34,56]
# l2 = [x//2 for x in l1]
# l3 = [x*2 for x in range(11)]



# l1 = [x*x for x in range(2,11,2)]
# for i, j in enumerate(l1):  // enumerate returns a tuple each time
#     print(i+1,j)
# for i in enumerate(l1):
#     print(i[0],i[1])
# for i in enumerate(l1):
#     print(i[0])




# l1 = [x for x in range(1,11)]
# l2 = [y for y in range(1,11)]
# l3 = [z for z in range(1,11)]
# for i,j,k in zip(l1,l2,l3):
#     print(i,j,k)




# student = {
#     "name": "Ali",
#     "age": 20
# }
# for key, value in student.items():
#     print(key, value)



# print("why".upper())
# print("WhY".lower())




# count = 10
# def inc():
#     global count
#     for i in range(5):
#         count += 1
#     return count
# print(inc())
# print(inc())




# simple = lambda a,b,c,d:a+b+(c*d)
# print(simple(23,23,4,9))
# easy = lambda a,b=34,c=3:a*b*c
# print(easy(9))



# num = [x for x in range(1,11)]
# result = list(map(lambda x:x+x*x,num))  # here function can also be used instead of lambda
# print(result)






# num = [x for x in range(1,11)]
# result = list(filter(lambda x:x%2==0,num))
# print(result)

# numbers = [1, 2, 3, 4, 5, 6]
# def is_even(x):
#     return x % 2 == 0
# evens = list(filter(is_even, numbers))
# print(evens)




# print("Hello"+" "+"world")
# s = "Hello how are you, Brothers And Sisters, are you all okay"
# print(s.endswith("okay"))
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.find("you"))
# print(s.replace("you","me"))
# print(s.count("s"))

# a = 45
# b = 34
# b,a = a,b
# print(a, b)

# a = 34
# b = 34
# print(a is b)
# print(hex(id(a)))
# print(hex(id(b)))




# list

# l = [23,34,25,71]
# m = [90,93,19,34]
# n = l + m
# print(n)
# print(n[::2])

#.append(x), .insert(index,x), .remove(x)(if try to remove a number that is not in the list gives error(ValueError))
# .pop() it removes last value, .sort(), .reverse(), .clear()
# count, .pop(3) to remove value at specific index, .copy(), sorted()


# l = ["Muhammad Atif",34,34,"why are you",34]
# l.insert(-1,34342)
# print(l)
# print(l.index("why are you"))   # it gives ValueError if element is not present in the list

# pairs = [
#     [1, 20],
#     [2, 30],
#     [3, 40],
#     [4, 50]
# ]
# for i,j in pairs:
#     print(i,"\t",j)

# numbers = [x for x in range(11)]
# # print(numbers*3)
# student = ["muhammad atif", 22, 3.57]
# my_lst = numbers + student  #lists concatenation





# tuples are immutable
# tup = ("34f3f3",3435,"why are you",90,34)
# print(tup.index("why are you",1,3))
# print(tup.index("why are you"))
# print(tup.count(34))
# t1 = (1,)
# t2 = ()
# print(type(t2))


# student = ("Ali", 21, "BSCS")      # a fixed record
# name, age, program = student       # unpacking
# print(name, age, program)




# sets
# each element in the set must be unique and immutable, set ignores repeated elements
# sets are mutable but set elements are immutable
# list and dictionary can't be stored inside set, as they are mutable 
# add,remove,clear ---> it empties the overall set,pop ---> remove and return a random value(KeyError if no element is presentin the set) 
# set1.union(set2) --> it return the union of the two sets, set.intersection(set2)

# -,|,&   difference, union, intersection





# dictionary 
# Keys are immutable so keys can't be list,dict,set b/c they are mutable    dict don't allow duplicate keys
# print(student.get("hello"))  # as no "hello" key is present, it will not give us error, but return None
# dict.update({"City":"Peshawar"})
# dict.update(student)
# del dict["key_name"]   or   dict.pop("key_name")           # use to delete key:value   pair  
# dict.pop("keys_name",None)    # it return   None if key does not exist
# item = dict.popitem()    # removes the last inserted value 
# get 


# dict = {
#     "names":34,
#     "gpa":4.0,
# }

# dict["names"] = "why"
# dict[0] = "hello"
# print(dict.get("34"))



# t = {"name":"Muhammad Atif",34:3,"CGPA":3.80,"courses":["ML","AI","CALCULUS","LINEAR ALGEBRA"]}
# t.update({"HOOOO HOOOO":"HAAAAA HAAAA"})
# # print(t[list(t.keys())[0]])

# t["courses"].append("Neural Networks")

# del t["name"]
# # t.pop("name")

# print(t)





# -----------------------------------------------------






# 1
# n = int(input("Enter a number : "))
# flag = 0
# for i in range(1,51):
#     if(i % n == 0):
#         print(i)
#         flag = 1
# if not flag:
#     print("No multiples found in the range")


# 2
# items = ["apple", "banana", "apple", "cherry", "banana", "date"]
# flag = 0
# new = []
# for i in range(len(items)):
#     flag = 0
#     for j in range(i+1,len(items) - i):
#         if (items[i] == items[j]):
#             flag = 1
#             break
#     if(flag != 1):
#         new.append(items[i]) 
# print(new)


# 3
# sentence = input("Enter a number : ")
# length  = 0
# for i in sentence:   # finding length without using len() function
    # length+=1
# words = 1
# longest = 0
# long = 0
# for i in range(len(sentence)-1):
#     if(sentence[i]==" " and sentence[i+1]!=" "):
#         words+=1
#     if(sentence[i]!=" " and i != len(sentence)):
#         long += 1
#     else:
#         longest = max(long, longest)
#         long = 0
# longest = max(long+1, longest)
# print(f"The length of the sentence is {length}")
# print(f"Number of words are {words}")
# print(f"The longest words size is {longest}")

# 4
# checking if a string is empty or not 
# s = ""
# if not s:
#     print("String is empty")
# else:
#     print("String is not empty")


# 5
# s = "abracadabra"
# d = []
# count = 1
# for i in range(len(s)):
#     count = 1
#     if(s[i] in d):
#         continue
#     for j in range(len(s)):
#         if(s[i] == s[j] and i != j):
#             count+=1
#     d.append(s[i])
#     d.append(count)
# print(d)



# 6
# n = int(input("Enter a number : "))
# m = n
# count = 0
# while(m):
#     count+=1
#     m //= 10
# m = n
# sum = 0
# while(m):
#     r = m % 10
#     sum += r**count
#     m //= 10
# if(sum == n):
#     print("It is !")
# else:
#     print("No brother")













# square = lambda x : x*x
# num = [square(x) for x in range(1,10)]
# print(num)


# s = ["Muhammad Atif",2.90,120012,"$",True,False]
# for i in s:
#     print(i,end="\t\t")
# print("\n")


# n = [x for x in range(1,21,3)]
# for i in range(7):
#     print(n[i])


# nums = [y*y+2 for y in range(1,11)]
# for i in range(-1,-11,-1):
#     print(nums[i],end="\t")
# print("\n")
# for i in range(10):
#     print(nums[i],end="\t")
# print("\n")



# n = [s for s in range(1,11)]
# print(n)
# print(len(n))


# square = lambda x:x*x 
# nums = [x for x in range(1,11)]
# m = list(map(square,nums))
# result = nums + m
# print(result)



# l = [56,67,45,6,4,54,5,34]
# num = [34,56,34,35,23]
# num.append(l)
# print(num)



# num = [34,56,34,35,23]
# num.extend(range(2,21,2))
# print(num)


# names = ["mango"]
# for i in names[0]:
#     print(i,end=" ")




# n = ["name","age","marks"]
# m = ["raaaajaaaa",13]
# for i,j in zip(n,m):
#     print(i,":",j)



# names = ["mango"]
# for i, j in zip(range(1,6,2),names[0]):
#     print(i,j,end=" ")



# names = ["mango"]
# for i, j in enumerate(names[0]):
#     print(i, j,end=" ")


# name = "Muhammad Atif"
# for i in range(1,len(name),2):
#     print(name[i],end="  ")


# n = [34,67,68,56,45]
# n.insert(-1,2323)
# print(n)



# n = [34,67,68,56,45]
# n.append([1,[45,567,768,"Why brother, why"]])
# n.append([x for x in range(10)])
# print(n)

# n.reverse()
# print(n)



# nam = ["Atif","Raja"]
# nam.sort()
# print(nam)

# nam.reverse()
# print(nam)




# names = ["Atif","Aizaz","Raja","Unknown"]
# new = []
# for i in names:
#     i = i.lower()
#     i = i[::-1]
#     new.append(i)
# new.sort()
# print(new)



# n = [62,23,45,56,234,67,56]
# m = n.pop()  # by default remove the last value
# print(m)
# n.pop(3)    # for deleting value at a specific index
# m = n.pop(-1)
# print(m)
# print(n)



# n = [62,23,45,56,234,67,56]
# n.sort(reverse=True)
# print(n)
# n.clear()
# print(n)


# matrix = [
#     [34,56,45,23],
#     [78,56,45],
#     [12],
#     [67,45,34,45]
# ]
# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#     print("\n")



# def show(x):
#     # print(x)   it can't be done here, if documents are added after an operation then __doc__ will not work and return None
#     """
#     Why am i so in love
#     mix a little bit of weed 
#     with a little bit of cash
#     with a little bit of this 
#     with a little bit of that
#     """
#     print(x)
# print(show.__doc__)   




# num = [45,67,23,67,3,67,23,66,33,22]
# def e(x):
#     if(x%2==0):
#         return x
# even = list(filter(e,num))                      # 1st way 
# even = list(filter(lambda x:x%2 == 0, num))     # 2nd way 
# print(even)





# filter(condition, iterable)

# filter() returns an iterator (a filter object) which can be iterated over or converted to a collection 
# type like a list or tuple.


# What happens if you pass None as the first argument to the filter function, such as 
# filter(None, [0, 1, False, 2, '', 'hello'])?
# Answer : When None is passed as the function, filter() uses the items' own boolean values to drop any 
# items that are falsy.
# n = list(filter(None, [0, 1, False, 2, '', 'hello']))
# print(n)

# If no elements match the condition, the filter iterator is empty, and converting it to a list yields 
# an empty list []

# l = list(filter(lambda s: len(s) > 3, ["apple", "cat", "dog", "banana"]))
# print(l)





# map(function, iterable)

# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x * x, numbers))
# print(squares)
# print(numbers)

# map() returns an iterator (a map object) which can be iterated over or converted to a collection type 
# like a list or tuple.


# What happens when you pass two iterables to map(), such as map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])
# Answer : map() takes elements from each iterable in parallel, passing them as arguments (x and y) to 
# the lambda function.




# n = list(map(lambda x, y: x + y, [1, 2], [10, 20, 30, 40]))
# m = list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))  # iterable object should be passed, by 
# # passing 5 or 2 etc gives error, as they are int and not iterable objects
# print(n)
# print(m)



# count = 0
# def i():
    # count += 1 # wrong
    # a global variable can be use inside a function but can't be changed
    # print(count)
    # if you wanna use it then global keyword is used with it
    # global count
    # count +=1
    # print(count)
# i()
# i()
# print(count)



# count = 10
# def increase():
#     # count = 20       # local variable
#     # print("Local:", count)
#     global count
#     print(count)

# increase()
# print(count)



# d = {
#     "name" : "Muhammad Atif",
#     "age" : 22, 
#     "gpa":4.0
# }
# for i,j in zip(d.keys(),d.values()):
#     print(i,"  ",j)



# colors = ["Red", "Green", "Blue"]
# for i, color in enumerate(colors):
#     print(i, color)


# fruits = ["Apple", "Banana", "Mango"]
# for i in enumerate(fruits): # i contains the entire tuple produced by enumerate().
#     print(i)
# for i in enumerate(fruits):
#     print(i[0])
#     print(i[1])

# for fruit in enumerate(fruits):
#     print(i, fruit)     # not allowed, i is not declared


# for i in "Why Brothers and sisters":
#     print(i,end=" ")
# print("\n")




# for i in range(3):
#     for j in range(4):
#         print(j,end=" ")
#     print("\n")


# you can make changes in loop to the global variable but not in function
# count = 1
# while count <= 5:
#     print(count)
#     count += 1



# print(2//4.0)  # floor function
# print(-(-2//4))# ceil function, e.g: -11//4 results in -3 as -2.75 rounds down to -3 and the second - converts in into +3


# print("Atif"*4)


# not 1
# and 2
# or  3


# name = None
# if name is None:
#     print("I know but why")



# student = {
#     "name": "Ali",
#     "age": 20,
#     "city": "Peshawar"
# }
# print("name" in student)
# print("name" in student.keys())
# print("Ali" in student.values())
# print(("name","Ali") in student.items())



# result = None
# if result is not None:
#     print(result)  #  nothing will print



# value = 2
# print(value is 2)  


# value = None
# print(value is None)   #  True
# Why is it strongly recommended to use x is None instead of x == None when checking if a variable is None in Python?
# Answer : None is a singleton in Python, and using is ensures you are checking its exact identity. 
# Custom classes can override __eq__ to return unexpected results when compared with == None.

# None is called a singleton because only one single instance of the NoneType object exists in 
# memory during the entire time your program runs.



# a = [45,5,34,46,23]
# b = a
# print(a is b)
# b[0] = 265
# print(a)
# print(b)
# print(a is b)
# a = [45,67,34,56,23]
# print(a is b)
# print(a)
# print(b)




# Given a = 100 and b = 100, what will a is b evaluate to, and why?

# a = 23
# b = 23
# print(a is b) # True because python pre-caches and reuses small integer objects in the range of -5 to 256.

# Correct! Python caches integers from -5 to 256 inclusive. When you assign numbers in this range, 
# both variables point to the same pre-allocated integer object in memory.

# a = 34
# b = 34
# print(hex(id(a)))
# print(hex(id(b)))

# a = -2652555
# b = -2652555
# print(a is b)  # True
# Note: Behavior can sometimes differ in a single script due to compiler optimizations, but separately 
# bound large numbers are not guaranteed to be identical identities




# a = 20000
# print(a is 20000) # it gives True in vs code and False in Jupyter notebook along with syntaxwarning

# a = 2
# print(a is 2) # it gives True in both along with syntaxwarning




# value_if_true if condition else value_if_false
# age = 17
# status = "Adult" if age >= 18 else "Minor"
# print(status)



# score = 90
# grade = "A" if score>=85 else ("B" if score>=75 else "C")
# print(score,grade)



# to keep it safe from DivisionByZeroError
# i = 3
# t = 500
# average = t/i if i>0 else 0
# print(average)


# numbers = [x for x in range(1,11)]
# labels = ["even" if x%2 == 0 else "odd" for x in numbers]
# print(numbers)
# print(labels)



# score = 34
# print(f"You {"passed" if score >= 50 else "fail"} the exam")







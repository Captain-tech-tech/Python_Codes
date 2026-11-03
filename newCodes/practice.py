# a = list(range(100))
# c=45
# while True:
#     print(a[c:c+1],end=" ") #it prints [45] not 45, b/c slicing always return a list
#     c+=3
#     if c==66:
#         break 
# print("\n")


# g = 345
# print(type(g))
# h=str(g)
# print(type(h))

# i = "2"
# b = 34
# print(int(i)+b)

# print(47/4,47%4,int(47/4))



########################################################################
# find, capitalize, replace, lower(), upper(), count, endswith  ---->  methods for strings
# indexing,slicing,  len,getsizeof, type
# slicing syntax    ----->   string[start:end:step]

# id(variable_name),hex(id(variable_name)) used for finding memory address of a variable
# The meaning of id() is implementation-dependent.
# Small integers and some strings may be reused (interned), so multiple variables can have the same id()


########################################################################
# lists are mutable, lists syntax  list=[45,67,34,56,23],   empty list ----> list=[]
# indexing,slicing same as strings,   nested list can also be made 

# student=["Muhammad Atif","25p0053",3.72,2]
# student[0]="Why are you here"  # as lists are mutable
# print(student)

# append,list.index(x) it results the index of first occurence,sort,sort(reverse=True),reverse like list.reverse ,insert(index_number,element),remove(element) remove first occurrence of an element
# list3.pop(4) # for deleting value at specific index,   list.copy()   ,  count
# sorted_list=sorted(list2) # use of sorted : it sort the list and return that sorted list, but the original list remains the same

# list=[34,56,67,23,56,23,59]


########################################################################
# tuples are immutable,   syntax tup=(45,56,"rg43",45.34),   indexes and slicing is the same as string 
# tup=() # empty tuple
# tup=(3,) # in case of tuple with one value   comma is necessary
# tup=(3)  # it is an integer
# tuple.index(value,start,end) or tuple.index(any_element) it return the index of first occurance,count
# value --> Element to find.
# start (optional) --> index where the search begins (inclusive).
# end (optional) --> index where the search stops (exclusive).



########################################################################
# dictionaries are used to store data values in key:value pairs,  
# Keys are immutable so keys can't be list,dict,set b/c they are mutable    dict don't allow duplicate keys
# Values can be of any data type
# syntax      
# dict={
#     key:value
# }
# dict.keys,dict.values,dict.items ---> it return all key:value pairs as tuples
# # +===== Accessing each pair =====+
# pairs=list(student.items())
# print(pairs[0],"\t",pairs[2])
# print(student.get("hello"))  # as no "hello" key is present, it will not give us error, but return None
# dict.update({"City":"Peshawar"})
# dict.update(student)
# del dict["key_name"]   or   dict.pop("key_name")           # use to delete key:value   pair  
# dict.pop("keys_name",None)    # it return   None if key does not exist
# item = dict.popitem()    # removes the last inserted value 
# get 

"""
# dictionary practice question
student={
    "Name":"Muhammad Atif",
    "Age":22,
    "marks":3.8,
    "Age":34    # duplicate keys are not allowed, here in this case the  "Age" key store this new value
}
print(student["Age"])
print(student.keys())

print(student.get("werg"))  # if no key is present, then it return None
student.update({"Goals":"AI security engineer"})
"""


# list = []
# str = ""
# tup = ()
# dict = {}
# set1 = set()
# print(list,str,tup,dict,set1)     # it is see how variables looks when empty



#####################################################################
# each element in the set must be unique and immutable, set ignores repeated elements
# sets are mutable but set elements are immutable
# list and dictionary can't be stored inside set, as they are mutable 
# only unique elements are stored

# set1={}   this is an empty dictionary
# set2=set()  an empty set 

# add,remove,clear ---> it empties the overall set,pop ---> remove and return a random value 
# set1.union(set2) --> it return the union of the two sets, set.intersection(set2)



#range functions
# range functions return a sequence of numbers, starting from 0 by default and increment by 1(by default) 
# and stops before a specified number
# range(start?,stop,step?) # ? means it is optional

#                 range=slicing

# for i in range(10):
#     pass      # by using pass empty loop can be created
# print("Helllllooooo0")
# if i>5:
#     pass      # pass is mainly used, if we wanna work on something in future


# *********************************************************************
# functions
# def greeting():
#     print("Hello",end=" ")
#     print("Brothers and sisters",end=" ")
#     print("How are you all today")
# greeting()

# def sum(a=4,b=5):
#     return a*b
# print(sum(5,6))


# def fact(a):
#     b=1
#     f=1
#     while b<=a:
#         f*=b
#         b+=1
#     return f
# print(fact(5))


# *********************************************************

# recurrsion
# def show(a):
#     if a==0:  # base case
#         return 1
#     print(a)
#     show(a-1)
# show(8)

# def show1(t):
#     if t==0: # base case
#         return 1
#     show1(t-1)
#     print(t) 
# show1(34)

# list is build in data type that stores set of different values or same values (int,float,string etc)
# strings are immutable in python while lists are mutable
marks=[45.6,67,89,97.7,67]
print(type(marks))
print(marks)

# for creating empty list
list4=[]

#indexing is allowed in python
print(marks[0],marks[2])
print(len(marks))
student=["Muhammad Atif","25p0053",3.48,3]
print(student)
student[0]="This is immutable"
print(student)


# list slicing is possible in list and same as string slicing
print(student[1:3])
print(student[2:])
print(student[2:len(student)])
print(student[:2])
print(student[-3:-1])


# list methods
list=[45,24,64,23,53]
list.append(34) #it does not return something, it append only new value
print(list)
print(list.sort()) # it gives us None, because it does not sort() function does not return something, it changes the original list
print(list)
print(list.sort(reverse=True)) # sorting in reverse order
print(list)
list1=["banana","apple","litchi","mango"]
list1.sort()
print(list1)
list2=[23,64,12,78,34]
sorted_list=sorted(list2) # use of sorted : it sort the list and return that sorted list, but the original list remains the same
print(list2,"\n",sorted_list)
list2.reverse()  # it is used for flipping the whole list
print(list2)
list3=[67,34,78,56,12,34,64,34]
print(list3)
list3.insert(2,1234) #list.insert(index,element)
print(list3)
list3.remove(34) # remove first occurrence of an element
print(list3)
list3.pop(4) # for deleting value at specific index
print(list3)    





print("\n\n\n\nTUPLES \n\n")

# tuple is build in data type in python that let us create immutable sequence of values
tup=(34,64,23,65,23,57,23)    
print(type(tup)) 
print(tup[2],tup[1]) # indexing is allowed in tuples
# tup[3]=35 # it is not allowed, as tuples are immutable
tup1=() #just creating empty tuple
print(tup1,type(tup1))
tup2=(1,) # correct way of creating tuple with one value, while in case of multiple values in tuple, using , at end is optional
print(tup2,type(tup2))
tup3=(1) # python will consider it as integer, if , is not used
print(tup3,type(tup3))

# slicing also works the same as in list and string
print(tup.index(23)) # return the index of the first occurence
print(tup.count(23)) # return total occurences



# practice questions

# program to ask the user to enter three favourite movies names and store them in list 
print("\nEnter three movies names")
list4.append(input("Enter your first movie name : "))
list4.append(input("Enter your second movie name : "))
list4.append(input("Enter your third movie name : "))
print("Your list of favourite movie : ",list4,"\n\n")
# program to check if a list contain palindrome of elements
list5=[]
print("Enter five values in a list")
# list5.append(input(),input(),input(),input(),input()) # append function can't take multiple values at once
list5.append(input())
list5.append(input())
list5.append(input())
list5.append(input())
list5.append(input())
# list6=list5 # here both list5 and list6 point to the same list in memory
list6=list5.copy()  # this create seperate copy, it is used for shallow copy 
list5.reverse()
if(list5==list6):
    print("The list is a palindrome\n")
else:
    print("The list is not a palindrome\n")    











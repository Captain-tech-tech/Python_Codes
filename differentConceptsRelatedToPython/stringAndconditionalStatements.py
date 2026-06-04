str="This is a string.\tHii hello how are you.\nWe are creating it in python"
print(str)
#concatenation
a="Hello "
b="World"
c=a+" "+b # it can be done for adding space between strings
print(a+b,"   ",c)
#len function
print(len(c))
z="Hello world","why are you here"
print(len(z))  # when multiple lines are present in a string seperated by ,   then len gives us the number of lines, not number of characters
#indexing        -----> accessing index out of range gives us error
d="Why are you here"
ch=d[0]
print(ch)
print(d[4]) # in python, values at indexes can only be accessed, it can't be changed through indexing
#slicing --> accessing parts of a string
str1="The one you seek is seeking you" 
print(str1[2:12]) #ending index is not included here only in this case,if end point is given then it does not display last index value
print(str1[4:len(str1)])
print(str1[2:]) # 2:len(str1)
print(str1[:12])  # 0:12
#slicing through negative indexing
str2="Why am i so in love"
print(str2[-8:-1])

# slicing syntax    ----->   string[start:end:step]

#string functions
str3="i am here just for you, am i okay."
print(str3.endswith("you.")) # return True if string ends with substring otherwise false
print(str3.capitalize()) # does not capitalize original string
str3=str3.capitalize() # we can do this for permanent capitalizing
print(str3.replace("e","a")) # it is use for replacing all e in string with a
print(str3.replace("you","me"))
print(str3.find("a")) #return index of first occurrer
print(str3.find("just"))
print(str3.find("q")) # if we search for something that does not exist, it gives us -1
print(str3.count("am"))



#Conditional statements
print("\n\nconditional statements\n",)
age1=int(input("Enter your age : "))
if(age1>=18):
    print("Your are eligible for voting")
    print("You can also drive")
elif(age1>=10 and age<18):
    print("You are a child, wait for a few years\n")
else:
    print("You are really small to even apply for license")
#nesting
age2=int(input("Enter your age : "))
if(age2>=18):
    if(age2>=90):
        print("Can't drive, too old, might have an accident")
    else:
        print("You can drive")
else:
    print("Can't drive bro, you are too young")




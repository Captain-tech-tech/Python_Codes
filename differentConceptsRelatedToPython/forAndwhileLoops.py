
# while True: # infinite while loop
#     print("why are you here")


# # -----_+_-----------_+_----------_+_-----------
count=0
while count<=5:
    print("How are you brother",count)  
    count+=1


# ==============+++++++++==================
i=1
while i<=100:
    print(i)
    i+=1   


# -=-=-=-=-=-=-=-=-=-=-=-=
j=100
while j>=1:
    print(j)
    j-=1


# -=-=-=-=-=-=-=-=-=-=-=-=    
n=float(input("Enter a number : "))  # input() returns a string by default, that's why type casting is necessary
m=1
while m<=10:
    print(n*m,"\n")
    m+=1;


# -=-=-=-=-=-=-=-=-=-=-=-=
tup=(45,57,23,76,34,68,25,87)
print("For which number you are looking in the tuple\n",tup)
k=float(input("Enter your favorite number : "))
l=0
q=0
while l<len(tup):
    if tup[l]==k:
        print("The number ",k,"is found at index",l)
        q=1
        break
    l+=1    
if q==0:
    print("No number like ",k,"is present in given tuple")


# _-=+_-=+_-=+_-=+_-=+_-=+_-=+_-=+_-=+_-=+_-=+_-=+
# break keyword
print("\n\n")
x=1
while x<=9:
    print(x)
    if(x==6):
        break
    x+=1


# ***--------***_______***---------***________
# continue keyword 
print("\n\n")
z=0
while z<=10: # it is mostly used for skipping values
    if z==6:
        z+=1
        continue #
    print(z)
    z+=1    
"""
"""


# for loop
list=[45,64,23,34,6452,232]
for ele in list:
    print(ele)
print("\n\n")    
tup=("how","are","you","what","are","you","doing","here")
for val in tup:
    print(val)
print("\n\n")    
str="Hello World"
for el in str:
    print(el)
print("\n\n")    
for el in str:
    if el=="o":
        print("o is found\n")
        break
    print(el)
else:
    print("END\n") 
"""
"""       


#range functions
# range functions return a sequence of numbers, starting from 0 by default and increment by 1(by default) 
# and stops before a specified number
# range(start?,stop,step?) # ? means it is optional
print(range(7))
print("\n\n")
seq=range(9)
for val in seq:
    print(val)
print("\n\n")
for i in range(12):
    print(i)
print("\n\n")
for i in range(2,10): # range(start,stop)
    print(i)
print("\n\n")
for i in range(2,10,2): # range(start,stop,step)
    print(i)
print("\n\n")
for i in range(100,1,-2):
    print(i)
print("\n\n")
"""
"""


# pass statement
# _-+_-=_-+_-=_-+_-=_-+_-=_-+_-=_-+_-=_-+_-=
# for i in range(10):
#     #empty  # something should be writtien in for block
# print("Hello world")
# _-+_-=_-+_-=_-+_-=_-+_-=_-+_-=_-+_-=_-+_-=
for i in range(10):
    pass # by using pass empty loop can be created
print("Helllllooooo0")
if i>5:
    pass # pass is mainly used, if we wanna work on something in future
"""
"""


# finding factorial of first n numbers
sum=1
for i in range(int(input("Enter n value upto which you wanna find factorial : "))):
    if i==0:
        print("0 ! = 1")
        continue
    else:    
        sum*=i;
        print(i,"! = ",sum)
















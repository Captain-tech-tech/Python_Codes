
# print(),len(),type(),range() are the build in functions 
print("Hello",end=" ") # by default end="\n" and , means sep=" "
print("World")  

# functions reduce redundancy and increase reusibility
# function definition
def cal_sum(a,b): # a and b are function parameters
    c=a+b
    return c
print(cal_sum(34,54)) # here 34 and 54 are function arguments
a=45
b=78
print(cal_sum(a,b))

# ++++++++++++++===========+++++++++++++
def greeting():
    print("Hello, how are you brothers!")
    print("Why are you here, what are you doing here")
greeting()
output=greeting()
print(output) # a function which does not return something, return None

#-=--==---===----====-----=====------======
# average of three numbers
def average(a,b,c):
    return (a+b+c)/3
print(average(36,34,22))

#++++++++++++++++++++++++++++++++
# default arguments
def multi(a=5,b=6): # parameter without a default follows parameter with a default
    print(a*b)
multi(357)
multi()
multi(9,8)

#=======++++++===========
#finding factorial of a number
def facto(a):
    if a==0:
        return 1
    else:   
        sum=1 
        for i in range(1,a+1):
            sum*=i
    return sum
print(facto(8))

#=+++==+++======+===+==++=+====+++===
# Recursion : when a funtion calls itself repeatedly
def show1(a):  # code for printing 1 to n numbers by recurrsion
    if a==0: # base case
        return
    print(a)
    show1(a-1)    
show1(5)


def show2(a):  # code for printing n to 1 numbers through recurrsion
    if a==0:  # base case
        return
    show2(a-1)
    print(a)
show2(5)


























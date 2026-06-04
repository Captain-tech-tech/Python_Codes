# string,float,int,bool,None
print("Hello world. ","My name is Muhammad Atif")
print(34)
print(35+23)
name="Muhammad Atif" #string     Hello()*(78
age=21 #int
price=34.2346 #float
print(name)
print(price)
name="Atif Khan"
print("My name is ",name)
age2=age
print(age2)
print(type(name))
print(type(age))
print(type(price))
print('hello world',"why are you here",'''What are you doing''') # all are correct
first=True
second=False
a=None
print(first,second,a)
print(type(a),type(second),type(first))
a=45
b=34
sum=a+b
print(sum)
# arithmatic operators(+,-,*,/,**,%) # in case of division, answer is always in floating form
# relational operators(==,!=,>,<,>=,<=)
# assignment operators(=,+=,-=,*=,/=,%=,**=)
# logical operators(not,and,or)
#Arithmatic Operators
print("arithmatic operator")
a=7
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a**3)
# Relational Operators
print(a==b,a!=b,a>=b,a<=b,a>b,a<b)
#assignment operators
print("assignment operator")
num=10
num+=num #num=num+10
print(num)
num/=3
print(num)
num*=3
print(num)
#logical operatorsLogical operator")
print(not False)
print(not True)
print(False and True)
print(False or True)
val1=True
val2=True
print(val1 and val2)
#type conversion
print("type conversion")
c=2
d=4.5
sum=c+d # 2.0+4.5 => 6.5  automatically done
print(sum)
#type casting
print("Type casting")
e="2" # character value string can't type caste
f=4
c=int(e)+f
print(c)
g=34
h=str(g)
print(type(h))
print("Taking input from user")
noom=input("Enter Your Name : ") # Result for input() is always a string
print(type(noom),"Welcome ",noom)
val=int(input("Enter your age : "))
print(type(val),val)
value=float(input("Enter your GPA : "))
print(type(value),value)
#simple practice questions
# write a program to enter two numbers and print there sum
a=int(input("Enter your first number : "))
b=int(input("Enter your second number : "))
print("The sum of your two numbers is : ",a+b)
#program for inputing side of a square and printing its area
s=float(input("Enter the length of the side of a square : "))
print("The area of the square is ",s**2)




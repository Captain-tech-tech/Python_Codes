# 01. Checking whether the user enter a vowel or not

# c = input("Enter a vowel : ")

# if c in 'aeiou' or c in 'AEIOU':   # or   if c.lower() in 'aeiou':
#     print(c,"is a vowel")
# else:
#     print(c,"is not a vowel")





# 02. reversing a string
# string = input("Enter a string : ")

# reverse_string = string[::-1]
# print(reverse_string)




# 03. printing the ASCII value of the char

# n = input("Enter a character :")
# print(ord(n))





# 04. converting number to character
# i = int(input("Enter a number : "))

# print(type(i))
# i = chr(i)
# print(type(i))





# 05. checking a palindrome
# string = input("Enter a string for checking, if it is a palindrome or not : ")

# reverse_str = string[::-1]

# if(string == reverse_str):
#     print(string,"is a palindrome")
# else:
#     print(string,"is not a palindrome")







# 06. sum of digits of a number
# n = int(input("Enter a number : "))
# count = 0
# sum = 0
# temp = n 
# while(temp != 0):
#     sum += (temp%10)
#     temp = temp//10
#     count+=1

# print(f"{n} has {count} digits and its sum is {sum}")



# 07. product of digits of a number

n = int(input("Enter a number : "))
product = 1
temp = n
while(temp != 0):
    product *= (temp%10)
    temp = temp//10

print("The product of the digits of ",n,"is",product)


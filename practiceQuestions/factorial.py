#  codes for understanding of functions and recurrsions


# finding factorial of a number through a function

# def fac(a):
#     fact=1;
#     if a<0:
#         print("Negative number have no factorial!")
#     elif a==0:
#         print("0! = 1")
#     elif a==1:
#         print("1! = 1")
#     elif a>1:
#         count=1
#         while count<=a:
#             fact*=count
#             count+=1
#         print(a,"! = ",fact)

# fac(-4),fac(0),fac(1),fac(5)





# finding factorial of a number through recursion

# def facto(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*facto(a-1)   # n!=n*(n-1)!

# print(facto(5))



# write a function to calclate sum of first n natural numbers using recursion

# def sum(a):
#     if a==0:
#         return 0
#     else:
#         return a+sum(a-1) 

# print(sum(5))




# recursive funtion to print all elements in a list,  using list and index as parameters

# def print_list_recursive(my_list, index=0):
#     # Base case: if index reaches the length of the list, stop
#     if index == len(my_list):
#         return
#     # Print the current element
#     print(my_list[index])
#     # Recursive call: move to the next index
#     print_list_recursive(my_list, index + 1)

# list = [10, 20, 30, 40, 50]
# print_list_recursive(list)

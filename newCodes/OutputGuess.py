# 01
# x = [1,2,3]
# y = x
# y.append(4)
# print(x)



# 02
numbers = [1, 2, 3, 4, 5, 6]
for x in numbers:
    numbers.remove(x)

print(numbers)



# this unexpected result happens because modifying a list while iterating over it breaks the 
# loop's internal counter. Python keeps track of where it is in the list using an implicit 
# index number (starting at 0, then 1, etc.). When you remove items, the remaining items shift left, 
# causing the loop to skip elements


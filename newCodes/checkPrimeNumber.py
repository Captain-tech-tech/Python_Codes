num = 7
if num > 1 and all(num % i != 0 for i in range(2,num)):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    




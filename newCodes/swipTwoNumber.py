a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(f"Before swipping a : {a} and b : {b}")

a, b = b, a 

print(f"After swipping a : {a} and b : {b}")


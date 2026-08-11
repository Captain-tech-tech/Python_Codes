n = int(input("Enter which fibonacci number you wanna find : "))

a, b = 0, 1

for _ in range(n):
    a, b = b, a + b

print(f"The {n}th fibonacci number is {a}")


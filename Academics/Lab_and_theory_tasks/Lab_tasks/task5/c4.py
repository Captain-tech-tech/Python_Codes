# question # 04

# for checking the condition, if the numbers satisfy the condition or not
def is_pythagorean(a,b,c):
    return a*a + b*b == c*c
# finding number of ordered triplets and printing them as well
n=0
for c in range(1, 31):
    for b in range(1, 31):
        for a in range(1, 31):
            if(is_pythagorean(a,b,c)):
                print(f"({a},\t{b},\t{c})")
                n += 1

print(f"Number of ordered triples:{n}")

# question # 02

# for finding the factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    i = 1
    for j in range(n,1,-1):
        i *= j
    return i

# fining the different possible combinations
def combination(n,r):
    if(n<0):
        print("(Invalid n value) : n values can't be less than 0")
    elif(n-r<0):
        print("(Invalid r value) : r<=n is the basic mathematical condition for finding combination")
    ans = (fact(n))/(fact(r)*fact(n-r))
    return int(ans)  # type cast to int because mathematically nCr is always an integer value

# n = int(input("Enter number of options (n value) :"))
# r = int(input("Enter number of choices you want (r value):"))
# ans = combination(n,r)

print(combination(10,3))
print(combination(6,2))

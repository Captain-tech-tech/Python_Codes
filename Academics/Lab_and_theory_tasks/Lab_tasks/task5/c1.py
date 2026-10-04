# Assignment # 01

# question # 01

# finding square root through babylonian method
def approximate_sqrt(n, guess=1.0, steps=8):
    '''
    approximate the square root of a number using babylonian method
    n = the number whose sqrt we wanna find
    guess = better initial guess can make it converge very fast, guess can't be zero b/c then it will cause ZeroDivisionError
    steps = how many times to perform the update, more steps better accuracy
    '''
    for i in range(steps):
        guess = (guess+ (n/guess))/2

    return guess
    

ans1 = approximate_sqrt(49)
ans2 = approximate_sqrt(2,1.0,10)

print(f"square root of 49 is {ans1}")
print(f"square root of 2 is {ans2}")

# guess controls where you start and steps controls how many times you improve the guess

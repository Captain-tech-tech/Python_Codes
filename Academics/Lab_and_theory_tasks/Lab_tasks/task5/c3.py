#  question # 03

# arithmetic progression nth term and sum of n terms

# finding the nth term of the sequence
def nth_term(n, a, d = 1):
    ans = a + (n-1)*d
    return ans

# finding the sum of digits in the sequence upto nth terms
def sum_ap(n, a, d = 1):
    '''
    finding sum of n terms of an arithmetic progression
    a = the first number of the sequence
    d = it is the common difference
    n = it is the nth term upto which we wanna find sum
    '''
    sum = (n/2)*(2*a + (n-1)*d)
    return sum

# printing the results
print("With default (common difference) d=1")
print("a10 = a1 + (n-1)d = ",nth_term(10,3))
print("S10 = n/2 (2a1 + (n-1)d) = ",sum_ap(10,3))

print("\nWith default (common difference) d=4")
print("a10 = a1 + (n-1)d = ",nth_term(10,3,4))
print("S10 = n/2 (2a1 + (n-1)d) = ",sum_ap(10,3,4))

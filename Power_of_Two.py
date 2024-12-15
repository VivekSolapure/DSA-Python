n=4
# Bit manipulation
print(n>0 and (n & (n-1))==0)
# number "n" should be greater than zero and every number that is power of 2 has exactly 1 number of 1s in binary representation
# so if we just do the AND OPERATION with the previous number of n (i.e n-1) we get 0 as value 


#Iteration

def power(n):
    if n<0:
        return False
    while n%2==0:
        n=n//2
    return n==1
print(power(4))
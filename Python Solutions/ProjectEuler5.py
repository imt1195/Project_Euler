#Problem 5: Smallest Multiple

from fractions import gcd

def lcm(a,b):
    return (a*b/gcd(a,b))

def smallestMultiple(num):
    multiple = 1
    for x in range(1,num):
        n = lcm(n,x)
    print("Smallest Multiple is: n")
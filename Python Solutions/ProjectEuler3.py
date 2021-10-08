# Problem 3: Largest prime factor
#find factors of 600851475143

from CommonFunctions import check_prime
mainNum = 600851475143
primeFactors = []

for num in range(1,mainNum+1):
    if mainNum % num == 0:
        if check_prime(num):
            # print(num)
            primeFactors.append(num)

print(primeFactors[-1])

# works, but there might be a faster way
# also gets the answer quickly, but doesn't finish going through every number for a while
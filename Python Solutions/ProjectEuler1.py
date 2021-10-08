#Problem 1: Multiples of 3 and 5

numSum = 0

#find all multiples of 3 or 5
for num in range(3,1000):
    if num % 3 == 0 or num % 5 == 0:
        numSum = numSum + num

#print out sum of those multiples
print("The sum of all numbers below 1000 that are divisible by 3 or 5 is: ", numSum)
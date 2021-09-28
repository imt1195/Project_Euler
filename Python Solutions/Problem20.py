from CommonFunctions import factorial
# from math import factorial

numberString = str(factorial(10))
sum = 0
for element in numberString:
    sum += int(element)
print(numberString, sum)

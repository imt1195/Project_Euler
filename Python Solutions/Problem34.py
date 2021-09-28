from CommonFunctions import factorial

# get the factorials of all single digit numbers
factorials = [factorial(1),factorial(2),factorial(3),
factorial(4),factorial(5),factorial(6),
factorial(7),factorial(8),factorial(9)]

sum = 0

for element in factorials:
    sum += element

print(sum)
# get the factorial of each digit in a number

# Problem 2: Even Fibonacci numbers

firstNum, secondNum = 0, 1 # Starting numbers for fibonacci sequence
evenSum = 0

#loop until secondNum goes over 4 million
#since anything + 0 is itself, it will not be added into the total sum of even numbered elements
while secondNum <= 4000000:
    tempNum = firstNum + secondNum
    if tempNum % 2 == 0:
        evenSum = evenSum + tempNum
    firstNum = secondNum
    secondNum = tempNum

print("The sum of all even number in the fibonacci sequence up to 4,000,000 is: ", evenSum)
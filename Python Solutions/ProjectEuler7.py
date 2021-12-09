from CommonFunctions import isPrime

num = 1
counter = 0
while(counter<10001):
    num = num+1
    if(isPrime(num)):
        counter = counter + 1

print(num)
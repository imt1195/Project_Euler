#Problem 4: Largest Palindrome product

from CommonFunctions import check_num_palindrome

product = 0

#for loops goes through 100 to 1000 to include 999 as a multiplier
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        result = num1 * num2
        if check_num_palindrome(result):
            if result > product:
                product = result

print("Largest palindrome product is: ", product)
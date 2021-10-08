def factorial(num):
    factorial = 1;
    for x in range(1, num+1):
        factorial = factorial*x
    return factorial
    
def check_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

def check_num_palindrome(num):
    div = 1
    while num/div >= 10:
        div *= 10
    while num != 0:
        lead = num // div
        trail = num % 10
        if lead != trail:
            return False
        num = (num % div) // 10
        div = div/100
    return True
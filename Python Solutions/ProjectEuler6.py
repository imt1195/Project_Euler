def sumOfSquare(n):
    sumOfSquares = 0
    squareOfSum = 0
    for x in range(1,n+1):
        squareOfSum = squareOfSum + x
        sumOfSquares = sumOfSquares + (x**2)
    squareOfSum = squareOfSum**2

    print("Sum of squares: ", sumOfSquares)
    print("Square of sum: ", squareOfSum)
    print("Difference: ", squareOfSum-sumOfSquares)

sumOfSquare(10)
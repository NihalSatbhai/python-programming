# Recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * (factorial(num-1))

result = factorial(5)
print(result)

# Without Recursion
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

# Test the function
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial(number)}")
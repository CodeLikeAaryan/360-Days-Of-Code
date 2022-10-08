# Program to print the factorial of the given input number
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


n = int(input('Enter the value of n'))
result = factorial(n)
print(f"The value of {n}! is {result}")

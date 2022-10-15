# Implement a python program to find the sum of digits of two numbers
def SumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10)+SumOfDigits(n//10)


print(SumOfDigits(543))

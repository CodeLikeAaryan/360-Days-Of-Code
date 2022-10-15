# Implement a program to write fibonacci series using python
def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

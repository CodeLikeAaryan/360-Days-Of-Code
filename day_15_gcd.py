# Python program to print the gcd of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))

# Python code to implement the power of any number
def calc_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base*pow(base, exp-1)


print(calc_power(4, 2))

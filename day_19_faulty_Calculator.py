# Exercise 2: Faulty Calculator
# 45*3=555 ,55+4=214 ,112-3=34
'''
Design the calculator which will correctly solve all the calculations except the following ones 
Your program should take the operator from the user and return the result 
'''

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = input("Enter the operator")
if a == 45 and b == 3 and c == "*":
    print("555")
elif a == 55 and b == 4 and c == "+":
    print("214")
elif a == 112 and b == 3 and c == "-":
    print("34")
elif c == "*":
    print(a*b)
elif c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(a/b)
else:
    print("Please check your input")

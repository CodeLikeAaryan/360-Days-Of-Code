# Implement a code to find palindrome of the given number
'''
for example 121 is a palindrome as if reversed the values will be the same 
but 123 is not a plaindrome as the number reversed will not result in the same value
'''
from turtle import numinput


number = int(input("Enter the number of your choice"))
temp = number
reverse = 0
while (number > 0):
    dig = number % 10
    reverse = reverse*10+dig
    number = number//10

if temp == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

'''
# Binary To Decimal Conversion
n = input("Enter the binary number to convert it into decimal number ")
l = list(n)
sum = 0
l.reverse()
print(l)
for i in range(len(l)):
    sum = sum+int(l[i])*2**i
print(sum)


# Decimal To Binary Conversion
def find(dec_num):
    if(dec_num == 0):
        return
    else:
        find(int(dec_num/2))
        print(dec_num % 2, end="")

find(9)

'''

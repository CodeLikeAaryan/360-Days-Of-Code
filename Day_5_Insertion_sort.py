# Insertion Sort using Python
size = int(input("Enter the Size "))
a = []
for i in range(size):
    value = int(input("Enter the elements"))
    a.append(value)
for i in range(1, size):
    t = a[i]
    j = i-1
    while j >= 0 and t < a[j]:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = t
print("The sorted array is ", a)

# Python program to implement bubble sort
size = int(input("Enter the size of the list"))
a = []
for i in range(size):
    value = int(input("Enter the elements for the list "))
    a.append(value)
for i in range(size):
    for j in range(0, size-i-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
print("Sorted Array is :", a)

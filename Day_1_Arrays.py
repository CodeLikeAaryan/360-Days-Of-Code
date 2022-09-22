# Adding elements to the array
'''
import array as arr
a = arr.array('d', [1.1, 1.2, 1.6])
a.append(4.1)
append function is used to add single element at the end of the array
print(a)

b = arr.array('d', [1.1, 1.2, 1.6])
b.extend([2.4, 4.4])
extend function is used to add more than one element to the end of the array
print(b)

c = arr.array('d', [1.1, 1.2, 1.6])
c.insert(2, 4.5)
Insert command is used to add an element at a specific positon in an array
print(c)

Pop function and remove function in python
pop function is used when you want to remove an element and return it
a = arr.array('d', [1.1, 2.2, 3.4, 3.7])
print("Popping the last element ", a.pop())
print("Popping the 4 element ", a.pop(2))
a.remove(1.1)
print(a)


Array concatentation : It is used to concatenate two arrays using a "+" symbol
import array as arr 
a=arr.array('d',[1.1,2.2,3.4,4.5])
b = arr.array('d', [6.1, 4.2, 5.4, 9.5])
c=arr.array('d')
c=a+b
print("The concatenated array resulted is ",c)

-> Slicing of array 
import array as arr
a = arr.array('d', [1.1, 3.4, 3.1, 4.5])
print(a[0:3])
'''

# Reversing the Array
'''
Reversing the array means to reverse the elements of array. Suppose the array is 1,2,3,4 then its reverse output will be : 4,3,2,1
 
 Code For reverse string 
def rev(t):
    n = len(t)
    i = 0
    j = n-1
    while i < j:
        tp = t[i]
        t[i] = t[j]
        t[j] = tp
        i += 1
        j -= 1


n = int(input("Enter n"))
lt = []
for i in range(0, n):
    lt.append(int(input()))
rev(lt)
print(lt)

----------------------->Linear Search<-------------------------
Code For Linear Search :

def search(list1, ele):
    list2 = []
    flag = False
    for i in range(len(list1)):
        if(ele == list1[i]):
            flag = True
            list2.append(i)
    if(flag == True):
        for i in list2:
            print("Element is found at index :", i)
    else:
        print("Searched Element is not found ")


list1 = [13, 15, 3, 54, 23, 3, 53, 23, 3]
ele = int(input("Enter the element you want to search"))
print(search(list1, ele))


'''




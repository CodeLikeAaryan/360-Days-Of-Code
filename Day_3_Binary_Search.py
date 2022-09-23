# --------------------------Program to implement Binary Search using Python --------------------
def binarySearch(list,target):
    right=len(list)-1
    left=0
    while left<=right:
        middle=(left+right)//2
        if target==list[middle]:
            return middle 
        elif target>middle:
            return middle+1 
        else:
            return middle-1 
        
    return -1

print(binarySearch([1,2,3,4,5,6,7,8],5))
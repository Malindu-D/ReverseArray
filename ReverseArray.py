from array import *

arr = array('i',[1,2,3,4,5,])

for e in arr:
    print(e, end=" ")
print()

range1 = int(len(arr)/2)

for i in range(range1):
    reverse = arr[i]
    arr[i] = arr[len(arr)-i-1]
    arr[len(arr)-i-1] = reverse

for e in arr:
    print(e, end=" ")

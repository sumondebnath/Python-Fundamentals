from array import *

arr = array('i', [1, 3, 5])
print(arr)

arr.append(7)
print(arr)

arr.insert(4, 9)
print(arr)

newArr = array('i', [11, 13, 15])
arr.extend(newArr)
print(arr)

arr.pop()
print(arr)

print(arr.index(13))

arr.reverse()
print(arr)

n = arr.count(15)
print(n)

lst = arr.tolist()
print(lst)


# Slice element in the array

print(arr[1:5])
print(lst[1:5])
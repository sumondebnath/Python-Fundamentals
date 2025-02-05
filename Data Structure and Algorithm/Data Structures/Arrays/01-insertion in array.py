import array as Arr

arr = Arr.array('i', [1, 2, 3, 4, 5])

arr.insert(0, 0)
arr.insert(6, 6)
arr.insert(4, 10)

print(arr)

arr1 = Arr.array('i')

for i in range(10):
    arr1.insert(i, int(input()))

print(arr1)
import array as Arr

def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = Arr.array('i', [10, 20, 30, 40, 50])

    print(Linear_Search(arr, 40))
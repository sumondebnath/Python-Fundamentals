
def Binary_Search(lst, x):
    left = 0
    right = len(lst)-1

    while left <= right:
        mid = (left+right) // 2

        if lst[mid] == x:
            return mid
        elif x < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":

    lst = [10, 20, 30, 40, 50]
    ele = 20

    print(Binary_Search(lst, ele))
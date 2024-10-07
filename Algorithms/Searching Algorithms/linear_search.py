

def Linear_Search(lst, x):
    position = 0

    while position < len(lst):
        if lst[position] == x:
            return position
        position += 1

    return -1


if __name__ == "__main__":

    # lst = [10, 11, 12, 15, 16, 18, 19, 20, 25, 30]
    # x = 20

    n = int(input())
    lst = []
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    x = int(input())

    print(Linear_Search(lst, x))
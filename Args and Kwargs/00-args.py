

def add(*args):
    print(args[1])
    print(args)
    print(type(args))

    sum = 0
    for n in args:
        # print(n)
        sum += n
    return sum


if __name__ == "__main__":
    sum = add(10, 20, 30, 40, 50, 60, 70)
    print(sum)
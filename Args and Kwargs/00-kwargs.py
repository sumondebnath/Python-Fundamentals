
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, val in kwargs.items():
        print(f"{key} -- {val}")

    print(kwargs["a1"])
    print(kwargs["a2"])


if __name__ == "__main__":
    calculate(a1=10, a2=20, s1=10, s2=20, m1=10, m2=20)
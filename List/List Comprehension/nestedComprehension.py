

cube = [[[i + j + k for k in range(2)] for j in range(3)] for i in range(2)]

result = [(i, j, k) for i in range(2) for j in range(3) for k in range(2)]


print(cube)

print(result)
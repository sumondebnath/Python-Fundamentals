from numpy import array

twoDarr = array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])

# print(twoDarr)

for i in twoDarr:
    for j in i:
        print(j, end=" ")
    print()
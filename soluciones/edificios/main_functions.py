"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# 10                                                                           P   P   P
#  9                                                                           P   P   P
#  8                                                                           P   P   P
#  7   X   X   X   X                                                           P   P   P
#  6   X   X   X   X                                                           P   P   P
#  5   X   X   X   X           M   M   M   M   M   M                           P   P   P
#  4   X   X   X   X   S   S   S   M   M   M   M   M                           P   P   P
#  3   X   X   X   X   S   S   S   M   M   M   M   M                           P   P   P
#  2   X   X   X   X   S   S   S   M   M   M   M   M   A   A   A   A   A       P   P   P
#  1   X   X   X   X   S   S   S   M   M   M   M   M   A   A   A   A   A       P   P   P
# 00  01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  

"""
from prototools import show_matrix


def w_h(arr):
    w = max(arr, key=lambda x: x[1])[1]
    h = max(arr, key=lambda x: x[2])[2]
    return w, h


C = ((0, 4, 7), (4, 7, 4), (7, 12, 5), (8, 17, 2), (17, 19, 0), (19, 21, 10))
W, H = w_h(C)
M = [[" " for _ in range(W)] for _ in range(H)]


def add_block(first, last, height):
    first = 0 if first == 0 else first - 1
    for i in range(H - height, H):
        for j in range(first, last):
            M[i][j] = "X"


def main():
    for f, l, h in C:
        add_block(f, l, h)
    show_matrix(M)


if __name__ == "__main__":
    main()

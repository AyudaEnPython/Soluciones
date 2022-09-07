"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un algoritmo que presente la siguiente estructura, utilizando 'while':

1       1
13      23
135     456
1357    78910
13579   1112131415
"""

# ----------------------------------------------------------------------------
i = 1
while i <= 10:
    j = 1
    while j <= i:
        print(j, end="")
        j += 2
    print()
    i += 2

# output:
# 1
# 13
# 135
# 1357
# 13579

# ----------------------------------------------------------------------------
i = k = 1
while i <= 5:
    j = 1
    while j <= i:
        print(k, end="")
        j += 1
        k += 1
    print()
    i += 1

# output:
# 1
# 23
# 456
# 78910
# 1112131415

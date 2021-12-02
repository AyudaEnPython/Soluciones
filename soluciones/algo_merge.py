"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def merge(left, right):
    merged_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list


def merge_sort(lista):
    length = len(lista)
    if length <= 1:
        return lista
    mid = length // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)
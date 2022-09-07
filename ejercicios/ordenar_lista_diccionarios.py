"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Output requerida:
Key = Operating System, Value = 79
Key = Networking, Value = 80
Key = Data Structure, Value = 85
Key = Database, Value = 91
Key = Java, Value = 95
Key = Math, Value = 98
"""
from typing import Dict, List, Union

HashMap = List[Dict[str, Union[str, int]]]

hashmap: HashMap = [
    {"Key": "Math", "Value": 98},
    {"Key": "Data Structure", "Value": 85},
    {"Key": "Database", "Value": 91},
    {"Key": "Java", "Value": 95},
    {"Key": "Operating System", "Value": 79},
    {"Key": "Networking", "Value": 80}
]


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_bubble_sort.py
def ordenar(arr: HashMap, key: str) -> HashMap:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    ordered_hashmap = ordenar(hashmap, "Value")
    # ordered_hashmap = sorted(hashmap, key=lambda x: x["Value"])
    for key in ordered_hashmap:
        print(f"Key = {key['Key']}, Value = {key['Value']}")


if __name__ == "__main__":
    main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
from typing import Any, Dict, List

data: List[Dict[str, Any]] = [
    {
        "Type": "A", "id": "1017", "next": {"name": "example1"},
        "prev": {"name": "example8"}, "processType": "FILTER",
    },
    {
        "Type": "B", "id": "1018", "next": {"name": "example2"},
        "prev": {"name": "example8"}, "processType": "FILTER",
        },
    {
        "Type": "B", "id": "1019", "next": {"name": "example3"},
        "prev": {"name": "example8"}, "processType": "FILTER",
        },
    {
        "Type": "A", "id": "1020", "next": {"name": "example4"},
        "prev": {"name": "example8"}, "processType": "FILTER",
        },
    {
        "Type": "A", "id": "1021", "next": {"name": "example5"},
        "prev": {"name": "SOL CLARA NACIONAL"}, "processType": "FILTER"
        },
    {
        "Type": "A", "id": "1022", "next": {"name": "example6"},
        "prev": {"name": "example8"}, "processType": "FILTER",
        },
    {
        "Type": "B", "id": "1023", "next": {"name": "example7"},
        "prev": {"name": "example8"}, "processType": "FILTER",
        },
]


def clean(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    result = []
    for dict_ in data:
        tmp = {}
        for k, v in dict_.items():
            if isinstance(v, dict):
                for k_, v_ in v.items():
                    tmp.update({k: v_})
            else:
                tmp.update({k: v})
        result.append(tmp)
    return result


df = pd.DataFrame(clean(data))
print(df)

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add docstring and tests.
"""
import pandas as pd
from prototools import retrieve_argname, tabulate, red

HEADERS = ["Source", "A", "B", "C"]

source_1 = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    }
)
source_2 = pd.DataFrame(
    {
        "A": [10, 11, 12],
        "B": [13, 14, 15],
        "C": [16, 17, 18]
    }
)


def concatenar(a, b):
    a["Source"] = retrieve_argname(a)
    b["Source"] = retrieve_argname(b)
    df = pd.concat([a, b], ignore_index=True)
    return df.reindex(columns=HEADERS)


df = concatenar(source_1, source_2)
data = df.values.tolist()
print(tabulate(
    data,
    headless=True,
    headers=HEADERS,
    border_type="double",
    title="Dataset",
    color=red,
))

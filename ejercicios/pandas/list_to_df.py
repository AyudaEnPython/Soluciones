"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd

data = [
    {
        'kind': '...',
        'etag': '23423',
        'stats': {
            'a': 1,
            'b': 2,
        }
    
    }
]

df = pd.json_normalize(data)
print(df)

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

import json

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
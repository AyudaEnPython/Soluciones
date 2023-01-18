"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import requests

r1 = requests.get("https://dummyjson.com/products/1").json()
r2 = requests.get("https://dummyjson.com/products/2").json()
print(f"Precios: {r1['price']}, {r2['price']}")

diff = r1["price"] - r2["price"]
print(f"Diferencia: {abs(diff)}")

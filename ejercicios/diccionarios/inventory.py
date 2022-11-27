"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

inventory = [
    {"name": "apple", "price": "25.00", "quantity": "5"},
    {"name": "kiwi", "price": "15.00", "quantity": "5"},
    {"name": "pepper", "price": "13.00", "quantity": "0"},
]


def has_product(inventory, product):
    for item in inventory:
        if product == item["name"]:
            return True
    return False


def main():
    product = input("Product: ")
    if has_product(inventory, product):
        print(f"{product} in stock!")
    else:
        print("Not in stock!")
        price = float(input(f"Price of {product}: "))
        quantity = int(input(f"Quantity of {product}:"))
        inventory.append(dict(name=product, price=price, quantity=quantity))
    print(inventory)


if __name__ == "__main__":
    main()

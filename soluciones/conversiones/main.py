"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu

import conversor as c


def main():
    menu = Menu()
    menu.add_options(
        ("Conversor de binario a decimal", c.bin_to_dec),
        ("Conversor de decimal a binario", c.dec_to_bin),
        ("Conversor de binario a hexadecimal", c.bin_to_hex),
        ("Conversor de hexadecimal a binario", c.hex_to_bin),
        ("Conversor de decimal a hexadecimal", c.dec_to_hex),
        ("Conversor de hexadecimal a decimal", c.hex_to_dec),
    )
    menu.run()


if __name__ == "__main__":
    main()

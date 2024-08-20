"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from models import Number
# pip install prototools
from prototools import Menu, int_input, str_input, handle_error
from prototools.colorize import magenta, yellow, cyan


@handle_error
def convert(user_input, type_):
    n = Number(user_input)
    print(n.roman if type_ == "numeral" else n.value)


@handle_error
def add_numbers(x, y):
    n = Number(x) + Number(y)
    print(n)


def main():
    menu = Menu(
        cyan("Roman numerals"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ("Number to roman", lambda: convert(
            int_input("Enter number: ", min=0), "numeral")),
        ("Roman to number", lambda: convert(
            str_input("Enter roman: "), "roman")),
        ("Addition", lambda: add_numbers(
            str_input("Enter first number or roman: "),
            str_input("Enter second number or roman: "),
        )),
    )
    menu.settings(
        style="double",
        color=magenta,
        options_color=yellow,
        separators=True,
    )
    menu.run()


if __name__ == "__main__":
    main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#!/user/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
# pip install prototools
from prototools import cyan, magenta, tabulate


def _parse_args():
    """Helper function to parse arguments."""
    parser = ArgumentParser(
        prog="calcular_sueldo",
        description=(
            "Calcula el sueldo de un trabajador"
        ),
        epilog="",
    )
    parser.add_argument(
        "sueldo",
        type=float,
        help="Sueldo base del trabajador",
    )
    parser.add_argument(
        "-v",
        "--ventas",
        nargs="+",
        type=float,
        help="Ventas del mes",
    )
    parser.add_argument(
        "-p",
        "--porcentaje",
        default=0.1,
        type=float,
        help="Porcentaje de ganancia por venta",
    )
    return parser.parse_args()


def main():
    args = _parse_args()
    sueldo_base = args.sueldo
    comision = (
        sum(args.ventas) * args.porcentaje
        if args.ventas else 0
    )
    data = [
        ["La comisión por las ventas es", cyan(comision)],
        ["El sueldo total es", cyan(sueldo_base + comision)],
    ]
    print(tabulate(data, headless=True, inner=True, color=magenta))


if __name__ == "__main__":
    main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent

from utils import get_response, save_results


def parse_args():
    parser = ArgumentParser(
        prog="AyudaEnPython",
        formatter_class=RawDescriptionHelpFormatter,
        description=dedent("""\
            AyudaEnPython
            -------------

            grupo: https://www.facebook.com/groups/ayudapython
            sitio: https://ayudapython.com

            Este programa permite obtener la información de una API.
        """),
        epilog=dedent("""\
            Ejemplo
            -------
            > main.py GET posts

            Contenido de response.json:
            {
                "method": "GET",
                "url": "https://jsonplaceholder.typicode.com/posts",
                "status": 200,
                "content-type": "application/json",
                "encoding": "UTF-8",
            }
        """)
    )
    parser.add_argument(
        "method",
        help=(
            "Método que se usará para llamar al API"
            "(GET, POST, PUT, DELETE)"
        ),
    )
    parser.add_argument(
        "resource",
        help=(
            "Recurso sobre el que se realizará la operación"
            "(posts, comments)"
        ),
    )
    parser.add_argument(
        "-id",
        "--resource_id",
        help="Identificador único del recurso",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.method and args.resource and args.resource_id:
        response, method = get_response(
            args.method, args.resource, args.resource_id
        )
        save_results(response, method)
    elif args.method and args.resource:
        response, method = get_response(args.method, args.resource)
        save_results(response, method)


if __name__ == "__main__":
    main()

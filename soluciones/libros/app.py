"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from flask import Flask, render_template, request

from main import Libro, Libros

app = Flask(__name__)
libros = Libros()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        codigo = request.form.get("codigo")
        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        categoria = request.form.get("categoria")
        libro = Libro(codigo, nombre, precio, categoria)
        libros.agregar(libro)
        return render_template("libros.html", libros=libros.libros)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

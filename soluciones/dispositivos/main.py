"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: mockup
"""
from flask import Flask, render_template, request, redirect
from typing import Dict, Union
# pip install prototools
from prototools import ProtoDB, textbox, text_align

data = ProtoDB("database/data")
app = Flask(__name__)


def _f(data: object, value: str) -> Dict[str, Union[int, str]]:
    data = data.get_data()
    for d in data:
        if d["id"] == int(value):
            return d


@app.route("/results/<result>", methods=["GET", "POST"])
def get_results(result):
    if request.method == "GET":
        data_ = _f(data, result)
        textbox(f"ID: {data_['id']} | IP: {data_['ip']}")
        text_align("DO some bunch of stuffs")
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html",
        results=data.get_data(),
    )


if __name__ == "__main__":
    app.run(debug=True)

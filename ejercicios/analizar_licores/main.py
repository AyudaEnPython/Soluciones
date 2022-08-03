"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Dict, List

URL = "https://www.beeradvocate.com/beer/?view=recent"
CONVERT = {
    "look": "apariencia",
    "smell": "aroma",
    "taste": "sabor",
    "feel": "sensacion",
    "overall": "puntaje",
}
ID = "rating_fullview_content_2"
LABELS = {
    "abv": "BAscore_norm",
    "detail": "muted",
}


@dataclass
class Cerveza:
    nombre: str
    cerveceria: str
    estilo: str
    abv: str
    puntaje: float
    aroma: str
    sabor: str
    sensacion: str
    apariencia: str

    def to_dict(self):
        return self.__dict__


def clean_up(s: str) -> Dict[str, float]:
    return {
        CONVERT[k]: float(v) for k, v in {k:v for k, v in (x.split(": ")
        for x in s.split(" | "))}.items()
    }


def scrape(url: str) -> List[Cerveza]:
    data = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all("div", id=ID)
    for element in elements:
        names = element.find_all("a")[1]
        types = element.find_all("a")[2]
        companies = element.find_all("a")[3]
        abvs = element.find("span", class_=LABELS["abv"])
        details = element.find_all("span", class_=LABELS["detail"])[1]
        for detail in details:
            if not detail.startswith("r"):
                for name, company, type_, abv in zip(
                    names, companies, types, abvs
                ):
                    data.append(Cerveza(
                        nombre=name,
                        cerveceria=company,
                        estilo=type_,
                        abv=abv,
                        **clean_up(detail),
                    ))
    return data


def main():
    cervezas = scrape(URL)
    df = pd.DataFrame.from_records([cerveza.to_dict() for cerveza in cervezas])
    df.to_csv("data/cervezas.csv", index=False)


if __name__ == '__main__':
    main()

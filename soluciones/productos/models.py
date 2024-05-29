"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, asdict
from datetime import datetime
# pip install prototools
from prototools import ProtoSqlite

from config import HEADERS


@dataclass
class Entity:
    name: str

    def get(self):
        return asdict(self)


@dataclass
class Client(Entity):
    lastname: str
    nin: int

    def info(self):
        return dict(zip(HEADERS["client"], self.get().values()))


@dataclass
class Product(Entity):
    mfg: datetime
    exp: datetime

    def info(self):
        _d = self.get() | {"state": self.get_state()}
        return dict(zip(HEADERS["product"], _d.values()))

    def get_state(self):
        exp = datetime.strptime(self.exp, "%Y-%m-%d")
        days_left = (exp.date() - datetime.now().date()).days
        if days_left < 0:
            return "vencido"
        elif days_left <= 5:
            return "por vencer"
        else:
            return "vigente"


class Database:

    def __init__(self):
        self.db = ProtoSqlite("data/data.db")

    def add_client(self, client):
        self.db.add("Client", client.get())

    def add_product(self, product):
        self.db.add("Product", product.get())

    def get_client(self, id_):
        try:
            return self.db.select("Client", f"nin= {id_}")
        except:
            return None

    def get_product(self, name):
        try:
            return self.db.select("Product", f"name = '{name}'")
        except:
            return None

    def get_product_id(self, id_):
        try:
            return self.db.select("Product", f"id = '{id_}'")
        except:
            return None

    def get_all_products(self):
        return self.db.get_all("Product")

    def associate(self, client_id, product_id):
        query = f"""
        INSERT INTO ClientProduct (client_id, product_id)
        VALUES ({client_id}, {product_id})
        """
        try:
            self.db.query(query)
            return True
        except Exception as e:
            return False

    def get_client_products(self, id_):
        client = self.get_client(id_)
        if client:
            query = f"""
                SELECT Product.* FROM Product
                JOIN ClientProduct ON
                Product.id = ClientProduct.product_id
                WHERE ClientProduct.client_id = {client[0]}
            """
            return self.db.execute(query)
        return None

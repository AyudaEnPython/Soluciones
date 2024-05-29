"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Category:
    name: str
    description: str
    products: List['Product'] = field(default_factory=list)


@dataclass
class Product:
    name: str
    description: str
    price: float
    stock: int
    category: Category = None


@dataclass
class Provider:
    name: str
    address: str
    phone: str
    supplies: List[Product] = field(default_factory=list)


@dataclass
class Store:
    name: str
    location: str
    capacity: int
    products: List[Product] = field(default_factory=list)


@dataclass
class Database:
    categories: List[Category] = field(default_factory=list)
    products: List[Product] = field(default_factory=list)
    providers: List[Provider] = field(default_factory=list)
    stores: List[Store] = field(default_factory=list)

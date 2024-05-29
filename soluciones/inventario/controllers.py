"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class BaseManager:

    def __init__(self, database) -> None:
        self.db = database

    def get_entity(self, entities, name):
        return next((e for e in entities if e.name == name), None)


class RecordManager(BaseManager):

    def register_category(self, category):
        self.db.categories.append(category)

    def register_product(self, product, category):
        category = self.get_entity(self.db.categories, category)
        if category:
            product.category = category
            category.products.append(product)
            self.db.products.append(product)
        else:
            print("Category not found.")

    def register_provider(self, provider):
        self.db.providers.append(provider)

    def register_store(self, store):
        self.db.stores.append(store)


class StockManager(BaseManager):

    def add_stock(self, product, quantity):
        product = self.get_entity(self.db.products, product)
        if product:
            product.stock += quantity
        else:
            print("Product not found.")

    def remove_stock(self, product, quantity):
        product = self.get_entity(self.db.products, product)
        if product:
            if product.stock >= quantity:
                product.stock -= quantity
            else:
                print("Not enough stock.")
        else:
            print("Product not found.")

    def total_value(self):
        return sum(p.price * p.stock for p in self.db.products)


class ReportManager(BaseManager):

    def __init__(self, database, stock_manager) -> None:
        super().__init__(database)
        self.stock_manager = stock_manager

    def get_entity_info(self, entities, name):
        entity = self.get_entity(entities, name)
        if entity:
            return entity
        else:
            print(f"{name} not found.")

    def get_product_info(self, product):
        return self.get_entity_info(self.db.products, product)

    def get_category_info(self, category):
        return self.get_entity_info(self.db.categories, category)

    def get_provider_info(self, provider):
        return self.get_entity_info(self.db.providers, provider)

    def get_store_info(self, store):
        return self.get_entity_info(self.db.stores, store)

    def report(self):
        print("Total stock value:", self.stock_manager.total_value())
        for category in self.db.categories:
            print(
                f"Category: {category.name}, "
                f"Products: {[p.name for p in category.products]}"
            )
        for provider in self.db.providers:
            print(
                f"Provider: {provider.name}, "
                f"Supplies: {[p.name for p in provider.supplies]}")
        for store in self.db.stores:
            print(
                f"Store: {store.name}, "
                f"Products: {[p.name for p in store.products]}"
            )


class MainController:

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_model(self.model)

    def run(self):
        self.view.run()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from controllers import (
    MainController,
    RecordManager,
    StockManager,
    ReportManager,
)
from views import MainView
from models import Database


def main():
    database = Database()
    record = RecordManager(database)
    stock = StockManager(database)
    report = ReportManager(database, stock)
    view = MainView()
    model = type('Model', (object,), {
        "database": database,
        "record_manager": record,
        "stock_manager": stock,
        "report_manager": report,
    })
    controller = MainController(model, view)
    controller.run()


if __name__ == "__main__":
    main()

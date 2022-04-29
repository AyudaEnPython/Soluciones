"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def load_data(min: int = 0, max: int = 10, size: int = 20) -> np.ndarray:
    return np.random.randint(min, max, size=size)


def statistics(ser: pd.Series) -> None:
    for _ in ("mean", "mode", "median"):
        print(f"{_}: {ser.__getattribute__(_)()}")


def show_plots(ser: pd.Series, arr: np.ndarray) -> None:
    _, axs = plt.subplots(1, 3, figsize=(15, 5))
    for _, type_ in enumerate(("bar", "pie")):
        ser.value_counts().plot(kind=type_, ax=axs[_])
    ser.quantile(arr).plot(kind="box", ax=axs[2])
    plt.show()


def main():
    data = load_data()
    ser = pd.Series(data)
    print(ser.value_counts())
    statistics(ser)
    show_plots(ser, np.arange(0.1, 1, 0.1))


if __name__ == "__main__":
    main()

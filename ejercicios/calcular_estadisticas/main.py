"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE:
- Algunas partes del enunciado no estan bien descritas.
- Las lineas 22, 23 y 24 se comentan para pasar los tests de la
    plataforma en la cual esta el ejercicio.
- Solo utilizar el codigo desde la línea 10 hasta la línea 29 (no usar
    las demás lineas)
"""
import pandas as pd


def calcular_estadisticas(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna un DataFrame con las estadisticas de los datos."""
    df = df[df["PAGO"] != 0].groupby("MODELO").agg({
        "USUARIO": "count",
        "PAGO": ["mean", "max", "min"],
        "ESTRELLAS": ["mean", "std"],
        "COMETARIO": "sum",
    })
    df.fillna(0, inplace=True)
    df.columns = [
        "CANTIDAD", "PROMEDIO", "MAXIMO", "MINIMO",
        "ESTRELLAS", "DESV. ESTRELLAS", "COMENTARIOS",
    ]
    # df.sort_values(by="MODELO", inplace=True)
    # df = df.reset_index()
    # df.set_index("MODELO", inplace=True)
    return df.round(2)


def main():
    df = pd.read_csv("data/data.csv")
    print(calcular_estadisticas(df))


if __name__ == "__main__":
    main()
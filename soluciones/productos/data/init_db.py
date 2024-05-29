"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sqlite3


def main(db_path, script_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(script_path, 'r') as file:
        sql_script = file.read()
    try:
        cursor.executescript(sql_script)
        print("Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main('data.db', 'create_tables.sql')

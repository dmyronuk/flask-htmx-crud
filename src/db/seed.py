from psycopg2 import connect
from pathlib import Path
import os
from db import create_connection


def execute_script(conn, filename: str):
    with conn.cursor() as cursor:
        p = Path(__file__).with_name(filename)
        with p.open("r") as sql:
            cursor.execute(sql.read())


def run():
    conn = create_connection()
    execute_script(conn, "down.sql")
    execute_script(conn, "up.sql")


if __name__ == "__main__":
    run()

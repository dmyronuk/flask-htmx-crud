from flask import g
from psycopg2 import connect, extras as psycopg2_extras
import os


def create_connection():
    conn = connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
    )
    conn.autocommit = True
    return conn


def get_db():
    if "db" not in g:
        g.db = create_connection()
    return g.db


def get_cursor():
    return get_db().cursor(cursor_factory=psycopg2_extras.DictCursor)


def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

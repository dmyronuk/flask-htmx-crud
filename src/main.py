from flask import Flask, request
from db.db import get_cursor

def create_app():
  app = Flask(__name__)

  @app.route("/todos")
  def todos():
    with get_cursor() as cur:
      cur.execute(
        'SELECT * FROM todos LIMIT %(limit)s;',
        {'limit': request.args.get('limit', 10)}
      )
      result = cur.fetchall()
      return [dict(row) for row in result]

  return app

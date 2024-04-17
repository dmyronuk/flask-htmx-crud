from flask import Flask, request, Response
from db.db import get_cursor
from datetime import datetime

def create_app():
  app = Flask(__name__)

  @app.get("/todos")
  def get_todos():
    with get_cursor() as cur:
      cur.execute(
        'SELECT * FROM todos LIMIT %(limit)s;',
        {'limit': request.args.get('limit', 10)}
      )
      result = cur.fetchall()
      return [dict(row) for row in result]

  @app.post("/todos")
  def create_todo():
    body = request.get_json()

    with get_cursor() as cur:
      cur.execute(
        """
          INSERT INTO todos (content, complete, created_at, updated_at) VALUES
          (%(content)s, false, %(created_at)s, %(created_at)s)
          RETURNING *;
        """,
        {
          'content': body['content'],
          'created_at': datetime.now().timestamp()
        }
      )
      result = cur.fetchone()
      return dict(result)

  @app.put("/todos/<id>")
  def update_todo(id):
    body = request.get_json()

    with get_cursor() as cur:
      cur.execute(
        """
          UPDATE todos SET content=%(content)s, updated_at=%(updated_at)s, complete=%(complete)s
          WHERE id=%(id)s
          RETURNING *;
        """,
        {
          'id': id,
          'complete': body['complete'],
          'content': body['content'],
          'updated_at': datetime.now().timestamp()
        }
      )
      result = cur.fetchone()
      return dict(result)

  @app.delete("/todos/<id>")
  def delete_todo(id):
    with get_cursor() as cur:
      cur.execute(
        'DELETE FROM todos WHERE id=%(id)s RETURNING *;',
        {'id': id}
      )
      return Response(status=200)

  return app



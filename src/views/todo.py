from flask import  request, Response
from flask.views import MethodView
from db.db import get_cursor
from datetime import datetime

class TodoAPI(MethodView):
  init_every_request = False

  def get(self, id = None):
    with get_cursor() as cur:
      cur.execute(
        'SELECT * FROM todos LIMIT %(limit)s;',
        {'limit': request.args.get('limit', 10)}
      )
      result = cur.fetchall()
      return [dict(row) for row in result]

  def post(self):
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

  def put(self, id: int):
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

  def delete(self, id: int):
    with get_cursor() as cur:
      cur.execute(
        'DELETE FROM todos WHERE id=%(id)s RETURNING *;',
        {'id': id}
      )
      return Response(status=200)


TodoView = TodoAPI.as_view('todos')
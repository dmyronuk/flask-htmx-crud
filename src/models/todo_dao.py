from datetime import datetime
from models.base_model import BaseModel
from psycopg2.extras import DictCursor

class TodoDAO(BaseModel):
  def __init__(self, conn):
    self.conn = conn

  def get_cursor(self):
    return self.conn.cursor(cursor_factory=DictCursor)

  def get_one(self, id: int):
    with self.get_cursor() as cur:
      cur.execute(
        'SELECT * FROM todos WHERE id=%(id)s;',
        {'id': id}
      )
      result = cur.fetchone()
      return dict(result) if result else None

  def get_many(self, limit=10):
     with self.get_cursor() as cur:
      cur.execute(
        'SELECT * FROM todos LIMIT %(limit)s;',
        {'limit': limit}
      )
      result = cur.fetchall()
      return [dict(row) for row in result]

  def create(self, todo: dict):
     with self.get_cursor() as cur:
      cur.execute(
        """
          INSERT INTO todos (content, complete, created_at, updated_at) VALUES
          (%(content)s, false, %(created_at)s, %(created_at)s)
          RETURNING *;
        """,
        {
          'content': todo['content'],
          'created_at': datetime.now().timestamp()
        }
      )
      result = cur.fetchone()
      return dict(result)

  def update(self, id: int, todo: dict):
     with self.get_cursor() as cur:
      cur.execute(
        """
          UPDATE todos SET content=%(content)s, updated_at=%(updated_at)s, complete=%(complete)s
          WHERE id=%(id)s
          RETURNING *;
        """,
        {
          'id': id,
          'complete': todo['complete'],
          'content': todo['content'],
          'updated_at': datetime.now().timestamp()
        }
      )
      result = cur.fetchone()
      return dict(result) if result else None

  def delete(self, id: int):
     with self.get_cursor() as cur:
      cur.execute(
        'DELETE FROM todos WHERE id=%(id)s RETURNING *;',
        {'id': id}
      )
      return '', 200

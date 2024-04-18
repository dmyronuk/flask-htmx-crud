from flask import Flask
from views.todo import TodoAPI
from models.todo_dao import TodoDAO
from db.db import get_db

def create_app():
  app = Flask(__name__)

  with app.app_context():
    conn = get_db()

    TodoView = TodoAPI.as_view('todos', TodoDAO(conn))
    app.add_url_rule("/todos", view_func=TodoView, methods=["GET", "POST"])
    app.add_url_rule("/todos/<int:id>", view_func=TodoView, methods=["GET", "PUT", "DELETE"])

  return app


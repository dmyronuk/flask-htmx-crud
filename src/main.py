from flask import Flask, render_template
from views.todo import TodoAPI, TodoView
from models.todo_dao import TodoDAO
from db.db import get_db

def create_app():
  app = Flask(__name__)

  with app.app_context():
    conn = get_db()

    todo_dao = TodoDAO(conn)
    todo_view_func = TodoView.as_view('todo_view', todo_dao)
    todo_api_view_func = TodoAPI.as_view('todo_api', todo_dao)

    app.add_url_rule("/todos", view_func=todo_view_func, methods=["GET", "POST"])
    app.add_url_rule("/todos/<int:id>", view_func=todo_view_func, methods=["GET", "PUT", "DELETE"])
    app.add_url_rule("/api/todos", view_func=todo_api_view_func, methods=["GET", "POST"])
    app.add_url_rule("/api/todos/<int:id>", view_func=todo_api_view_func, methods=["GET", "PUT", "DELETE"])

    @app.route('/')
    def index():
      return render_template('index.html')

  return app


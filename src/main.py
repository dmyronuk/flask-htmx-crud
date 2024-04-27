from flask import Flask, render_template
from views.todo import TodoAPI, TodoView
from models.todo_dao import TodoDAO
from db.db import get_db

def create_app():
  app = Flask(__name__)
  app.jinja_env.trim_blocks = True
  app.jinja_env.lstrip_blocks = True

  with app.app_context():
    conn = get_db()

    @app.route('/')
    def index():
      return render_template('index.html')

    @app.route('/todos/new')
    def new_todo():
      return render_template('todo_form_new.html')

    todo_dao = TodoDAO(conn)
    todo_view_func = TodoView.as_view('todo_view', todo_dao)
    todo_api_view_func = TodoAPI.as_view('todo_api', todo_dao)

    app.add_url_rule("/todos", view_func=todo_view_func, methods=["GET", "POST"])
    app.add_url_rule("/todos/<int:id>", view_func=todo_view_func, methods=["GET", "PUT", "DELETE"])
    app.add_url_rule("/api/todos", view_func=todo_api_view_func, methods=["GET", "POST"])
    app.add_url_rule("/api/todos/<int:id>", view_func=todo_api_view_func, methods=["GET", "PUT", "DELETE"])

  return app


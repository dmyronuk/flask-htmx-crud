from flask import Flask
from views.todo import TodoView

app = Flask(__name__)
app.add_url_rule("/todos", view_func=TodoView, methods=["GET", "POST"])
app.add_url_rule("/todos/<int:id>", view_func=TodoView, methods=["GET", "PUT", "DELETE"])

if __name__ == '__main__':
  app.run()

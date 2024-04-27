from flask import make_response, request, render_template, redirect
from flask.views import MethodView
from models.base_model import BaseModel

class TodoAPI(MethodView):
  init_every_request = False

  def __init__(self, model: BaseModel):
    self.model = model

  def get(self, id = None):
    if id:
      todo = self.model.get_one(id)
      return (todo, 200) if todo else ('', 404)
    else:
      return self.model.get_many(request.args.get('limit', 10))

  def post(self):
    return self.model.create(request.get_json())

  def put(self, id: int):
    return self.model.update(id, request.get_json())

  def delete(self, id: int):
    self.model.delete(id)
    return ('', 204)


class TodoView(MethodView):
  init_every_request = False

  def __init__(self, model: BaseModel):
    self.model = model

  def get(self, id = None):
    if id:
      todo = self.model.get_one(id)
      if todo:
        return render_template('todo_form_edit.html', todo=todo)
      else:
        return redirect('/404')

    else:
      todos = self.model.get_many(request.args.get('limit', 10))
      return render_template('todo_list.html', todos=todos)

  def post(self):
    todo = self.model.create(request.form)
    response = make_response(render_template('todo_form_edit.html', todo=todo))
    response.headers.set('HX-Trigger', 'createTodo')
    return response

  def put(self, id: int):
    todo = self.model.update(request.form.get('id'), {**request.form, 'complete': request.form.get('complete', False)})
    response = make_response(render_template('todo_form_edit.html', todo=todo))
    response.headers.set('HX-Trigger', 'updateTodo')
    return response

  def delete(self, id: int):
    self.model.delete(id)
    return ('', 200, {'HX-Trigger': 'deleteTodo'})

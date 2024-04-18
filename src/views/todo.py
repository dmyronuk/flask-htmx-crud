from flask import request
from flask.views import MethodView
from models.base_model import BaseModel

class TodoAPI(MethodView):
  init_every_request = False

  def __init__(self, model: BaseModel):
    self.model = model

  def get(self, id = None):
    if id:
      todo = self.model.get_one(id)
      return todo, 200 if todo else '', 404
    else:
      return self.model.get_many(request.args.get('limit', 10))

  def post(self):
    return self.model.create(request.get_json())

  def put(self, id: int):
    return self.model.update(id, request.get_json())

  def delete(self, id: int):
    self.model.delete(id)
    return '', 204

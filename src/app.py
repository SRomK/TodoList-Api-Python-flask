from flask import Flask, jsonify
from flask import request
import json
app = Flask(__name__)

todos= [{ "label": "My first task", "done": False }]
   


@app.route('/todos', methods=['GET'])

def hello_world():
    task = jsonify(todos)
    return task

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)

    todos.append(request_body)

    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    deleted_position = position
    print("This is the position to delete: ",deleted_position)
    todos.pop(deleted_position)
    

    return jsonify(todos), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
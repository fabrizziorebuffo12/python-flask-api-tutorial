from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista global de tareas
todos = [
    {
        "label": "My first task",
        "done": False
    }
]


# GET - Obtener todas las tareas
@app.route('/todos', methods=['GET'])
def hello_world():

    return jsonify(todos)


# POST - Agregar una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():

    request_body = request.json

    todos.append(request_body)

    return jsonify(todos)


# DELETE - Eliminar una tarea por posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    todos.pop(position)

    return jsonify(todos)


# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
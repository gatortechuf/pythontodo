from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

todos = {}
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todo/")
def get_todos():
    return jsonify(todo=todos)

@app.route("/todo/", methods=['POST'])
def create_todo():
    todo = request.get_json()
    if len(todos) == 0:
        todos[0] = todo['name']
    else:
        todos[max(todos.keys()) + 1] = todo['name']
    return jsonify(todo=todos)

@app.route("/todo/<int:id>")
def read_todo(id):
    todo = todos[id]
    return jsonify(todo=todos)

@app.route("/todo/<int:id>", methods=['PUT'])
def update_todo(id):
    todo = request.get_json()
    todos[id] = todo['name']
    return jsonify(todo=todos)

@app.route("/todo/<int:id>", methods=['DELETE'])
def delete_todo(id):
    todos.pop(id, None)
    return jsonify(todo=todos)

if __name__ == "__main__":
    app.run()

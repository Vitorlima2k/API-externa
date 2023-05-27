import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    return jsonify(data), 201

@app.route('/todos', methods=['DELETE'])
def delete_todos():
    return jsonify({"message": "Todos deleted"}), 200

if __name__ == '__main__':
    app.run()

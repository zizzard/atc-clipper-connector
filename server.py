from flask import  Flask, request, jsonify
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    content = request.json
    print(content)
    return content

@app.route('/add', methods=['POST'])
def add():
    content = request.json
    print(content)
    return content

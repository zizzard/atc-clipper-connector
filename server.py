from flask import  Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

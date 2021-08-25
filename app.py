from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import swag_from, Swagger
import os

app = Flask(__name__)
Swagger(app)

@app.route('/')
def main():
    return 'Please give 2 numbers in the path in /<number1>/<number2> format'


@swag_from(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template', 'app.yml'))
@app.route('/add', methods=['POST'])
def add():
    input1 = request.json
    addition = int(input1['n1']) + int(input1['n2'])
    return jsonify({'sum': addition})


app.run(port=5009, debug=True)
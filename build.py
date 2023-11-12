from os import fdopen
from flask import Flask, render_template, request
from flask.json import jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json
import charts

app = Flask(__name__)
CORS(app)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

result = "0"

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/post', methods=['POST'])
def update():
    global result
    KPIs =  json.loads(request.data.decode())
    first = float(KPIs['faddr'])
    second = float(KPIs['taddr'])
    result = first * second
    charts.generateGraphs(result)

    return "Grafer skapas"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')


@app.route('/get', methods=['GET'])
def getResult():
    global result
    return str(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
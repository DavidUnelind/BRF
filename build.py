from os import fdopen
from flask import Flask, render_template, request
from flask.json import jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json
import charts

app = Flask(__name__)
CORS(app)
app.secret_key = "dljsaklqk24e21cjn!Ew@@dsa5"

result = "0"

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/post", methods=["POST"])
def waterfall():
    global result
    KPIs = json.loads(request.data.decode())
    totalKostnad = float(KPIs["totalKostnad"])
    resultat = float(KPIs["resultat"])
    finansiellaKostnader = float(KPIs["finansiellaKostnader"])
    jämförelsestörande = float(KPIs["jämförelsestörande"])
    avskrivning = float(KPIs["avskrivning"])
    amortering = float(KPIs["amortering"])
    avsättning = float(KPIs["avsättning"])
    result = resultat
    charts.generateWaterfall(totalKostnad, 
                          resultat, 
                          finansiellaKostnader, 
                          jämförelsestörande,
                          avskrivning,
                          amortering,
                          avsättning)

    return "Grafer skapas"

@app.route("/postNyckelTal", methods=["POST"])
def nyckelTal():
    global result
    KPIs = json.loads(request.data.decode())
    totalLån = float(KPIs["totalLån"])
    totalYta = float(KPIs["totalYta"])
    boarea = float(KPIs["boarea"])
    intäkt = float(KPIs["intäkt"])
    underhållsutrymme = float(KPIs["underhållsutrymme"])
    driftskostnad = float(KPIs["driftskostnad"])
    charts.generateNyckeltal(totalLån, 
                          totalYta, 
                          boarea, 
                          intäkt,
                          underhållsutrymme,
                          driftskostnad)

    return "Grafer skapas"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")


@app.route("/get", methods=["GET"])
def getResult():
    global result
    return str(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
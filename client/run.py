from flask import Flask, request, jsonify, render_template
import json
import consignment_cli

app = Flask(__name__)

@app.route("/")
def main():
     return render_template('/index.html')

@app.route("/getConsignment", methods = ['POST'])
def getConsignment():
    payload = request.get_json()
    return jsonify(json.loads(consignment_cli.get_consignment(int(payload['consignment_id']))))

@app.route("/getVessel", methods = ['POST'])
def getVessel():
    payload = request.get_json()
    return jsonify(json.loads(consignment_cli.get_vessel(int(payload['id']), payload['name'], int(payload['weight']))))

if (__name__ == "__main__"):
    app.run(threaded=True, debug=True) 
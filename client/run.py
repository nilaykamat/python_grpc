from flask import Flask, request, jsonify, render_template
import json
import shipment_cli

app = Flask(__name__)

# Rendering Template for UI
@app.route("/ui")
def main():
     return render_template('/index.html')


# this will hit shipment service 
@app.route("/getShipment", methods = ['POST'])
def getShipment():
    payload = request.get_json()
    return jsonify(json.loads(shipment_cli.get_shipment(int(payload['shipment_id']))))

# this will hit carrier service through shipment service
@app.route("/getCarrier", methods = ['POST'])
def getCarrier():
    payload = request.get_json()
    return jsonify(json.loads(shipment_cli.get_carrier(int(payload['id']), payload['name'], int(payload['weight']))))

if (__name__ == "__main__"):
    app.run(threaded=True, debug=True, host='0.0.0.0') 

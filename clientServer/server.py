from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

#health check point which response the Ok when server is runnning 
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

#ping check point which response the pong when server is connected with client 
@app.route('/ping', methods=['POST'])
def ping():
    if request.is_json:
        data = request.get_json()
        if data.get('type') == 'ping':
            response = {
                "type": "pong",
                "time": datetime.utcnow().isoformat()
            }
            return jsonify(response), 200
    return jsonify({"error": "Invalid request"}), 400


@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        data = request.get_json()
        if data.get("jsonrpc") == "2.0" and data.get("method") == "message-1":
            response = {
                "jsonrpc": "2.0",
                "method": "message-1",
                "time": datetime.utcnow().isoformat()
            }
            return jsonify(response), 200
    return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

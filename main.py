from flask import Flask, request, jsonify

HOST = "10.1.9.88"
PORT = 8888
app = Flask(__name__)


@app.route("/", methods=["GET"])
def serve_home():
    return jsonify({
        'response': "Connected to backend."
    })


@app.route("/sampleResponse", methods=["POST"])
def serve_sampleResponse():
    data = request.json
    message = data['message']
    print("Message received: " + message)
    return jsonify({
        'response': f"Successfully received {message}."
    })


if __name__ == "__main__":
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)

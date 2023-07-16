from flask import Flask, request, jsonify
import base64

HOST = "10.1.254.188"
PORT = 8888
app = Flask(__name__)


@app.route("/", methods=["GET"])
def serve_home():
    return jsonify({
        'response': "Connected to backend."
    })


@app.route("/capturePhoto", methods=["POST"])
def serve_sampleResponse():
    data = request.json
    file = data['file']
    imgdata = base64.b64decode(file + "==")
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return jsonify({
        'response': "Successfully received photo."
    })


if __name__ == "__main__":
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)

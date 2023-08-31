from app import app
import firebase_admin


HOST = "10.1.7.78"
PORT = 8888

if __name__ == "__main__":
    cred = firebase_admin.credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred)
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(debug=True, host=HOST, port=PORT)

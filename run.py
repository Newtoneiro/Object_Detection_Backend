from app import app
import firebase_admin


# HOST = "10.1.7.78"
HOST = "192.168.137.173"
PORT = 8888

if __name__ == "__main__":
    cred = firebase_admin.credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred)
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)

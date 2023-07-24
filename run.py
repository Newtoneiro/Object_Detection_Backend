from app import app


HOST = "10.1.7.78"
PORT = 8888

if __name__ == "__main__":
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)

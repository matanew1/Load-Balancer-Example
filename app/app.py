from flask import Flask, request, Response, jsonify
from datetime import datetime
import socket
from pymongo import MongoClient, errors

app = Flask(__name__)

MONGO_URI = 'mongodb+srv://matan:matan@cluster0.bgo3pus.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

try:
    client = MongoClient(MONGO_URI)
    db = client['whist_cloud']
    counter_collection = db['counter']
    access_log_collection = db['access_log']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    counter_collection = None
    access_log_collection = None

initialized = False

def get_internal_ip():
    return socket.gethostbyname(socket.gethostname())

@app.before_request
def startup_event():
    global initialized
    if not initialized:
        try:
            if counter_collection is not None and counter_collection.find_one() is None:
                counter_collection.insert_one({'count': 0})
            initialized = True
        except Exception as e:
            print(f"Error initializing application: {e}")

# Routes and other functions
@app.route("/", methods=["GET"])
def read_root():
    try:
        counter_collection.update_one({}, {'$inc': {'count': 1}})
        client_ip = request.remote_addr
        server_ip = get_internal_ip()
        access_log_collection.insert_one({'date_time': datetime.now(), 'client_ip': client_ip, 'server_ip': server_ip})
        server_ip_response = {"internal_ip": server_ip}
        response = jsonify(server_ip_response)
        response.set_cookie(key="internal_ip", value=server_ip, max_age=300)
        return response, 200
    except Exception as e:
        return str(e), 500

@app.route("/showcount", methods=["GET"])
def show_count():
    try:
        counter = counter_collection.find_one()['count']
        counter_response = {"counter": counter}
        return jsonify(counter_response), 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


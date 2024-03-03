# routes.py
from flask import Blueprint, request, jsonify
from business_logic import BusinessLogic
import socket
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define a blueprint
bp = Blueprint('my_blueprint', __name__)

# Load business logic
business_logic = BusinessLogic(os.getenv('MONGO_URI'))

def get_internal_ip():
    return socket.gethostbyname(socket.gethostname())

@bp.before_request
def startup_event():
    business_logic.data_access.initialize_application()

@bp.route("/", methods=["GET"])
def read_root():
    try:
        client_ip = request.remote_addr
        server_ip = get_internal_ip()
        response_data = business_logic.process_request(client_ip, server_ip)
        response = jsonify(response_data)
        response.set_cookie(key="internal_ip", value=server_ip, max_age=300)
        return response, 200
    except Exception as e:
        return str(e), 500

@bp.route("/showcount", methods=["GET"])
def show_count():
    try:
        counter_response = business_logic.get_counter()
        return jsonify(counter_response), 200
    except Exception as e:
        return str(e), 500

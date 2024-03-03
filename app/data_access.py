# data_access.py
from database import Database  # Import the Database class

class DataAccess:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri
        self.db = Database(self.mongo_uri)  # Create an instance of Database
        self.counter_collection = self.db.counter_collection
        self.access_log_collection = self.db.access_log_collection

    def initialize_application(self):
        self.db.initialize_application()  # Call the method from Database

    def update_counter(self):
        self.db.update_counter()  # Call the method from Database

    def log_access(self, client_ip, server_ip):
        self.db.log_access(client_ip, server_ip)  # Call the method from Database

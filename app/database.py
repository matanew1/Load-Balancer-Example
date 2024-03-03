# database.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime

class Database:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri
        self.client = MongoClient(self.mongo_uri)
        try:
            self.db = self.client.whist_cloud
            self.counter_collection = self.db.counter
            self.access_log_collection = self.db.access_log
        except ConnectionFailure as e:
            print(f"Error connecting to MongoDB: {e}")
            self.counter_collection = None
            self.access_log_collection = None

    def initialize_application(self):
        if self.counter_collection is not None and self.counter_collection.find_one() is None:
            self.counter_collection.insert_one({'count': 0})

    def update_counter(self):
        if self.counter_collection is not None:
            self.counter_collection.update_one({}, {'$inc': {'count': 1}})

    def log_access(self, client_ip, server_ip):
        if self.access_log_collection is not None:
            self.access_log_collection.insert_one({'date_time': datetime.now(), 'client_ip': client_ip, 'server_ip': server_ip})

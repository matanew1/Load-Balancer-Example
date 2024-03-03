# business_logic.py
from data_access import DataAccess


class BusinessLogic:
    def __init__(self, mongo_uri):
        self.data_access = DataAccess(mongo_uri)

    def process_request(self, client_ip, server_ip):
        self.data_access.initialize_application()
        self.data_access.update_counter()
        self.data_access.log_access(client_ip, server_ip)
        return {"internal_ip": server_ip}

    def get_counter(self):
        try:
            counter = self.data_access.counter_collection.find_one()['count']
            return {"counter": counter}
        except Exception as e:
            return str(e), 500

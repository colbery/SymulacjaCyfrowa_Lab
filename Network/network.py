class Network:
    def __init__(self, base_stations):
        self.base_stations = base_stations
        self.users = []
        
    def add_user(self, user):
        self.users.append(user)
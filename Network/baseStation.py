class BaseStation:
    def __init__(self, station_id, location, capacity):
        self.station_id = station_id
        self.location = location
        self.capacity = capacity
        self.connected_users = []
        
    def connect_user(self, user):
        if len(self.connected_users) < self.capacity:
            user.connect(self)
            self.connected_users.append(user)
            return True
        else:
            return False
        
    def disconnect_user(self, user):
        user.disconnect()
        self.connected_users.remove(user)
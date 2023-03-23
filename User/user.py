class User:
    def __init__(self, user_id, location):
        self.user_id = user_id
        self.location = location
        self.connected = False
        self.current_station = None
        
    def connect(self, station):
        self.connected = True
        self.current_station = station
        
    def disconnect(self):
        self.connected = False
        self.current_station = None
    
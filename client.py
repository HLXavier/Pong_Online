import socket
import pickle


class Client:

    # Basic address information
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 5050
        self.addr = self.ip, self.port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player = None

    def connect(self):
        # Joining local server
        self.connection.connect(self.addr)
        self.player = pickle.loads(self.connection.recv(2048))
        return self.player

    def send(self, player):
        self.player = player
        self.connection.send(pickle.dumps(self.player))
        return pickle.loads(self.connection.recv(2048))




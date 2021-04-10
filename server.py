import socket
import threading
import pickle
from player import Player
from ball import Ball

# Game info
WIDTH = 1200
HEIGHT = 960

# Basic address information
ip = socket.gethostbyname(socket.gethostname())
port = 5050
addr = ip, port

# Creating local server
local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_server.bind(addr)

players = [Player(10, HEIGHT / 2 - 70, 10, 140), Player(WIDTH - 20, HEIGHT / 2 - 70, 10, 140)]
ball = Ball(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30)


# Threaded every time a client connects to the server
def handle_connection(conn, player_id):
    conn.send(pickle.dumps(players[player_id]))

    while True:
        client_response = conn.recv(2048)

        if not client_response:
            break
        players[player_id] = pickle.loads(client_response)

        if player_id == 0:
            conn.send(pickle.dumps([players[1], ball]))
        else:
            # We put the ball here so it will only be moved in players 1 thread.
            # Only ween player 1 entered the game.
            ball.move(WIDTH, HEIGHT, players[0], players[1])
            conn.send(pickle.dumps([players[0], ball]))

    print('Client disconnected')
    conn.close()


def start():
    player_id = 0
    print('Starting server')
    local_server.listen(2)

    while True:
        conn, client_addr = local_server.accept()
        print('{0} connected'.format(client_addr))
        thread = threading.Thread(target=handle_connection, args=(conn, player_id))
        thread.start()
        player_id += 1


start()

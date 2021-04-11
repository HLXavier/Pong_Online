import socket
import threading
import pickle
import pygame
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
score = [0, 0]


# Ball movement loop
def serve():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        point = ball.move(WIDTH, HEIGHT, players[0], players[1])
        if point > -1:
            score[point] += 1
            ball.set_speed(0, 0)
            pygame.time.wait(3000)
            ball.set_speed(9, 9)


# Threaded every time a client connects to the server
def handle_connection(conn, player_id):
    conn.send(pickle.dumps(players[player_id]))

    while True:
        client_response = conn.recv(2048)
        if not client_response:
            break
        players[player_id] = pickle.loads(client_response)
        if player_id == 0:
            conn.send(pickle.dumps([players[1], ball, score]))
        else:
            conn.send(pickle.dumps([players[0], ball, score]))

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

        if player_id == 2:
            serve()


start()

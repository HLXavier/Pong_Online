import pygame
import client

pygame.init()

WIDTH = 1200
HEIGHT = 960
SIZE = WIDTH, HEIGHT

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

# Game colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


def render(scr, player, opponent, ball):
    scr.fill(bg_color)
    # Half field line
    pygame.draw.aaline(scr, light_grey, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.draw.rect(scr, light_grey, player.rect)
    pygame.draw.rect(scr, light_grey, opponent.rect)
    pygame.draw.ellipse(scr, light_grey, ball.rect)


# Game loop
def start():
    running = True
    cli = client.Client()
    player = cli.connect()

    # Waiting for the other player to connect

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        clock.tick(144)
        server_response = cli.send(player)
        opponent = server_response[0]
        ball = server_response[1]
        render(screen, player, opponent, ball)
        player.move(HEIGHT)


start()

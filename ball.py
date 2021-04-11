import pygame
import random
import math


class Ball:
    def __init__(self, x, y, width, height):
        self.speed_x = 9
        self.speed_y = 9
        self.dx = 1
        self.dy = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, screen_width, screen_height, player, opponent):
        # Player collision
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.dy = random.uniform(0, 0.5) * random.choice([-1, 1])
            print(self.dy)
            self.dx *= -1

            #self.speed_x += 0.05
            #self.speed_y += 0.05

        # Top, Bottom  collision
        if self.y < 0 or self.y + self.height > screen_height:
            self.speed_y *= -1

        # Left collision
        if self.x < 0:
            self.center(screen_width, screen_height)
            # Player 1 point
            return 1

        # Right collision
        if self.x + self.width > screen_width:
            self.center(screen_width, screen_height)
            # Player 0 point
            return 0

        self.x += self.speed_x * self.dx
        self.y += self.speed_y * self.dy

        self.update()

        return -1

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def center(self, screen_width, screen_height):
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2 - 15
        self.update()

    def set_speed(self, x, y):
        self.speed_x = x
        self.speed_y = y
        self.dx = 1 * random.choice([-1, 1])
        self.dy = 0




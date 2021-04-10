import pygame


class Player:
    def __init__(self, x, y, width, height):
        self.speed = 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, screen_height):
        keys = pygame.key.get_pressed()

        # Up
        if keys[pygame.K_UP]:
            self.y -= self.speed
            if self.y < 0:
                self.y = 0

        # Down
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            if self.y + self.height > screen_height:
                self.y = screen_height - self.height

        # Update rect
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
import pygame

class Ball:
    def __init__(self, x, y, width, height):
        self.speed_x = 4
        self.speed_y = 4
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, screen_width, screen_height, player, opponent):
        # Player collision
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.speed_x *= -1

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

        self.x += self.speed_x
        self.y += self.speed_y

        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def center(self, screen_width, screen_height):
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2
        self.update()




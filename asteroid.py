import pygame
import circleshape
import main
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        #self.position = pygame.math.Vector2(x, y)
        self.radius = radius
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

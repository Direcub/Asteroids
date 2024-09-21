import pygame
import random
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            number = random.uniform(20, 50)
            badnumber = number * -1
            vel1 = pygame.math.Vector2.rotate(self.velocity, number)
            vel2 = pygame.math.Vector2.rotate(self.velocity, badnumber)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, vel1 * 1.2)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, vel2 * 1.2)
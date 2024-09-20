import pygame
from player import *
from constants import *
from asteroidfield import *
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    player.containers = (drawable, updatable)
    asteroidfield = AsteroidField()
    player1 = player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
            for thing in asteroids:
                if thing.collision(player1) == True:
                    print("Game over!")
                    exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
        

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import *
from pygame.color import THECOLORS

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        screen.fill(THECOLORS['black'])

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        
       
        for obj in asteroids:
            if obj.colliding(player):
                print("Game over!")
                return

        dt = clock.tick(60)/1000
        

       
if __name__ == "__main__":
    main()
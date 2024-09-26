import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
from asteroid import *
from pygame.color import THECOLORS

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable) 
   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0 
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in asteroids:
            if obj.colliding(player):
                print("Game over!")
                return

        for obj in updatable:
            obj.update(dt)
           

        screen.fill(THECOLORS['black'])

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            for  bullet in bullets:
                if asteroid.colliding( bullet):
                    points_earned = asteroid.split()
                    score += points_earned
                    bullet.kill()

        score_text = font.render(f"Score: {score}", True, THECOLORS['white'])
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        
       
      

        dt = clock.tick(60)/1000
       

       
if __name__ == "__main__":
    main()
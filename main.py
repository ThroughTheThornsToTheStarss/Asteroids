# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
pygame.init()
clock = pygame.time.Clock()
dt = 0 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
from pygame.color import THECOLORS
def main() :
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(THECOLORS['black'])
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
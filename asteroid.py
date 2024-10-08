import pygame
import random
from constants import *
from circleshape import CircleShape
GRAY = (177,115,64)
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius ) 
        
    def draw(self, screen):
        pygame.draw.circle(screen, GRAY, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return POINTS_FOR_ASTEROID 
        
        angle = random.uniform(20, 50)
         
           
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)
            
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 =Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 =Asteroid(self.position.x, self.position.y, new_radius)
      
        
        asteroid1.velocity = new_vector1 *1.2
        asteroid2.velocity = new_vector2 *1.2
        
        return 0
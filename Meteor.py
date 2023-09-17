import pygame, random
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

class Meteor(pygame.sprite.Sprite):
    def __init__(self, direction, currentPosition, speed):
        super().__init__()
        self.degree = random.randint(0, 360)
        self.image = pygame.image.load("./images/Projectile.png")
        self.rect = self.image.get_rect()
        self.rect.center = currentPosition
        self.direction = direction
        self.speed = speed
        self.collided = False

    def update(self):
        self.moveForward()
        self.checkBorderHit()

    def moveForward(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)

    def draw(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.degree), self.rect)
    
    def checkBorderHit(self):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH or self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.collided = True

    def destroy(self):
        self.collided = True
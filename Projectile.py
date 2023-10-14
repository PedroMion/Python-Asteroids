import pygame
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SPEED = 15


class Projectile(pygame.sprite.Sprite):
    def __init__(self, direction, currentPosition, degree):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load("./images/Projectile.png"), degree)
        self.rect = self.image.get_rect()
        self.rect.center = currentPosition
        self.direction = direction
        self.collided = False

    def update(self, meteorList, status):
        self.moveForward()
        self.checkColision(meteorList, status)
        self.checkBorderHit()

    def moveForward(self):
        self.rect.move_ip(self.direction[0] * SPEED, self.direction[1] * SPEED)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def checkColision(self, meteorList, status):
        for meteor in meteorList:
            collide = self.rect.colliderect(meteor.rect)
            if collide:
                status.increaseScore(meteor.type)
                meteor.destroy()
                self.collided = True
    
    def checkBorderHit(self):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH or self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.collided = True

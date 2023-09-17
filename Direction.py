import pygame
from pygame.locals import *
from Projectile import Projectile

FPS = 24
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
MAX_SPEED = 15
MIN_SPEED = 5
DEFAULT_DIRECTION = pygame.Vector2(0, -1)


class Direction(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = DEFAULT_DIRECTION
        self.degree = 0
        self.speed = MIN_SPEED
    
    def setAtributtes(self, direction, degree, speed):
        self.direction = direction
        self.degree = degree
        self.speed = speed
    
    def rotateLeft(self):
        self.degree = (self.degree + 15) % 360
    
    def rotateRight(self):
        self.degree = (self.degree - 15) % 360

    def changeDirection(self):
        self.direction = DEFAULT_DIRECTION.rotate(self.degree * (-1))

    def increaseSpeed(self):
        if(self.speed <= MAX_SPEED):
            self.speed += (MAX_SPEED - MIN_SPEED) / (2 * FPS)
    
    def decreaseSpeed(self):
        if(self.speed >= MIN_SPEED):
            self.speed -= (MAX_SPEED - MIN_SPEED) / (2 * FPS)
    
    def setMinSpeed(self):
        self.speed = MIN_SPEED
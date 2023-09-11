import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 24
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SPACESHIP_SIZE_IN_PIXELS = 17
MAX_SPEED = 20
MIN_SPEED = 10
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FramePerSec = pygame.time.Clock()

pygame.display.set_caption("Asteroids")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = pygame.Vector2(1, 0)
        self.speed = MIN_SPEED
        self.degree = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.handleKeyPress(pressed_keys)

        self.move()
    
    def move(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)

    def handleKeyPress(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rotateLeft()
        if pressed_keys[K_RIGHT]:
            self.rotateRight()
        if pressed_keys[K_UP]:
            self.increaseSpeed()
        else:
            self.decreaseSpeed()

    def increaseSpeed(self):
        if(self.speed <= MAX_SPEED):
            self.speed += (MAX_SPEED - MIN_SPEED) / FPS
    
    def decreaseSpeed(self):
        if(self.speed >= MIN_SPEED):
            self.speed -= (MAX_SPEED - MIN_SPEED) / FPS
    
    def rotateLeft(self):
        self.degree += 15
        self.direction = self.direction.rotate(15)
        self.direction = self.direction.normalize()
    
    def rotateRight(self):
        self.degree -= 15
        self.direction = self.direction.rotate(-15)
        self.direction = self.direction.normalize()

    def draw(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.degree), self.rect)

Player = Spaceship()

playerAlive = True
while playerAlive:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

    Player.update()

    DISPLAYSURF.fill((0,0,0))

    Player.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
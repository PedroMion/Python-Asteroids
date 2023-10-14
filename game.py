import pygame, sys
from pygame.locals import *
from Spaceship import Spaceship
from Enemies import Enemies
from Time import Time
from Status import Status

pygame.init()

FPS = 24
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FramePerSec = pygame.time.Clock()

pygame.display.set_caption("Asteroids")

Player = Spaceship()
Meteors = Enemies()
GameStatus = Status()
Clock = Time(FPS)

while Player.playerAlive:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
   
    Player.update(Meteors.meteors, GameStatus)
    Meteors.update(Clock.getTime())

    DISPLAYSURF.fill((0,0,0))

    Player.draw(DISPLAYSURF)
    Meteors.draw(DISPLAYSURF)
    GameStatus.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
import pygame
from pygame.locals import *

pygame.init()

font = pygame.font.SysFont("Monospace", 15, True, True)
space = 15

class Text(pygame.sprite.Sprite):
    def __init__(self, message, rectPosition):
        self.message = message
        self.pygameText = font.render(self.message, True, (255,255,255))
        self.rect = self.pygameText.get_rect()
        self.rect.center = rectPosition
    
    def update(self, message, rectPosition):
        self.message = message
        self.pygameText = font.render(self.message, True, (255,255,255))
        self.rect = self.pygameText.get_rect()
        self.rect.center = rectPosition
    
    def draw(self, surface):
        surface.blit(self.pygameText, self.rect)


class Status(pygame.sprite.Sprite):
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.playerAlive = True
        self.scoreText = Text("Score: " + str(self.score), (space*3, space))
        self.livesText = Text("Lives remaining: " + str(self.lives), (space*6, space*2))
    
    def draw(self, surface):
        self.scoreText.draw(surface)
        self.livesText.draw(surface)

    def decreaseLives(self):
        self.lives -= 1
        if self.lives == 0:
            self.playerAlive = False
            return
        self.livesText.update("Lives remaining: " + str(self.lives), (space*6, space*2))
    
    def increaseScore(self, meteorType):
        if meteorType == "Big":
            self.score += 10
        else:
            self.score += 5
        
        self.scoreText.update("Score: " + str(self.score), (space*3, space))
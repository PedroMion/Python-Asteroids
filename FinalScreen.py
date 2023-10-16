import pygame
from pygame.locals import *
from Status import Text

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

font = pygame.font.SysFont("Monospace", 15, True, True)

class FinalScreen(pygame.sprite.Sprite):
    def __init__(self):
        self.finalScore = 0
        self.firstText = Text("You died!", ((SCREEN_WIDTH // 2) - 10, (SCREEN_HEIGHT // 2) - 10))
        self.scoreText = Text("Final score: " + str(self.finalScore), ((SCREEN_WIDTH // 2) + 10, (SCREEN_HEIGHT // 2) + 10))
    
    def draw(self, surface):
        self.firstText.draw(surface)
        self.scoreText.draw(surface)
    
    def setScore(self, newScore):
        self.finalScore = newScore
        self.scoreText.update("Final score: " + str(newScore), ((SCREEN_WIDTH // 2) + 10, (SCREEN_HEIGHT // 2) + 10))
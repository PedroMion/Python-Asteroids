import pygame, os
from pygame.locals import *
from Status import Text

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FILENAME = "record.txt"

font = pygame.font.SysFont("Monospace", 15, True, True)

class FinalScreen(pygame.sprite.Sprite):
    def __init__(self):
        self.finalScore = 0
        self.recordScore = 0
        self.firstText = Text("You died!", ((SCREEN_WIDTH // 2) - 20, (SCREEN_HEIGHT // 2) - 20))
        self.scoreText = Text("Final score: " + str(self.finalScore), ((SCREEN_WIDTH // 2) - 10, SCREEN_HEIGHT // 2))

        self.initFile(FILENAME)
        self.readRecordScore(FILENAME)

        self.recordText = Text("Your record: " + str(self.recordScore), ((SCREEN_WIDTH // 2) -10, (SCREEN_HEIGHT // 2) + 20))

    
    def draw(self, surface):
        self.firstText.draw(surface)
        self.scoreText.draw(surface)
        self.recordText.draw(surface)
    
    def setScore(self, newScore):
        self.finalScore = newScore
        self.scoreText.update("Final score: " + str(newScore), ((SCREEN_WIDTH // 2) - 10, SCREEN_HEIGHT // 2))

        self.readRecordScore(FILENAME)
        if self.finalScore > self.recordScore:
            self.writeRecordScore(FILENAME, self.finalScore)
            self.recordText.update("New record: " + str(self.recordScore), ((SCREEN_WIDTH // 2) -10, (SCREEN_HEIGHT // 2) + 20))
    
    def initFile(self, fileName):
        if os.path.exists(fileName):
            with open(fileName, 'r') as record:
                self.recordScore = record.read()
            record.close()
        else:
            with open(fileName, "w") as record:
                record.write("0")
            record.close()
    
    def readRecordScore(self, fileName):
        with open(fileName, "r") as record:
            self.recordScore = int(record.read())

        record.close()
    
    def writeRecordScore(self, fileName, score):
        with open(fileName, "w") as record:
            record.write(str(score))
        
        record.close()
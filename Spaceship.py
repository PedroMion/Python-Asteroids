import pygame
from pygame.locals import *
from Projectile import Projectile
from Direction import Direction

FPS = 24
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
MAX_SPEED = 15
MIN_SPEED = 5
MAX_LIVES = 3
DEFAULT_DIRECTION = pygame.Vector2(0, -1)
CENTER_POSITION = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Spaceship.png")
        self.imageBoosting = pygame.image.load("./images/Spaceship_turbo.png")
        self.rect = self.image.get_rect()
        self.playerLives = MAX_LIVES
        self.startPlayer()

    def update(self, meteorList):
        pressed_keys = pygame.key.get_pressed()
        self.checkMeteorHit(meteorList)
        self.handleKeyPress(pressed_keys)
        self.updateAllProjectiles(meteorList)
        self.checkBorderHit()
        self.move()
        self.checkImmortality()

        self.ageInPosition += 1

    def updateAllProjectiles(self, meteorList):
        for projectile in self.projectiles:
            projectile.update(meteorList)
            if(projectile.collided):
                self.projectiles.remove(projectile)
                del projectile
    
    def move(self):
        direction = self.movement.direction
        speed = self.movement.speed
        self.rect.move_ip(direction[0] * speed, direction[1] * speed)

    def handleKeyPress(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.moveForward()
        else:
            self.movement.decreaseSpeed()
            self.movingForward = False

        if not self.movingForward:
            if pressed_keys[K_LEFT]:
                self.movement.rotateLeft()
            if pressed_keys[K_RIGHT]:
                self.movement.rotateRight()

        if pressed_keys[K_SPACE]:
            self.newProjectile()
        else:
            self.spacePressed = False

    def moveForward(self):
        self.movingForward = True
        if(self.movement.direction == DEFAULT_DIRECTION.rotate(self.movement.degree)):
            self.movement.increaseSpeed()
        else:
            self.movement.setMinSpeed()
            self.movement.direction = DEFAULT_DIRECTION.rotate(self.movement.degree * (-1))
    
    def newProjectile(self):
        if self.spacePressed == False:
            currentDirection = DEFAULT_DIRECTION.rotate(-self.movement.degree)
            projectile = Projectile(currentDirection, self.rect.center, self.movement.degree)

            self.projectiles.append(projectile)
        self.spacePressed = True

    def checkMeteorHit(self, meteorList):
        for meteor in meteorList:
            if self.rect.colliderect(meteor.rect) and self.immortal == False:
                self.meteorPlayerChock()
                return

    def checkBorderHit(self):
        if self.ageInPosition < 24:
            return
        
        if self.rect.left <= 0:
            self.rect.left = SCREEN_WIDTH
            self.ageInPosition = 0
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = 0
            self.ageInPosition = 0
        elif self.rect.top <= 0:
            self.rect.top = SCREEN_HEIGHT
            self.ageInPosition = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.ageInPosition = 0

    def meteorPlayerChock(self):
        self.playerLives -= 1
        if self.playerLives <= 0:
            self.playerAlive = False
            return
        self.startPlayer()
    
    def checkImmortality(self):
        self.timeAliveInFrames += 1
        if self.timeAliveInFrames == (FPS * 3) and self.immortal == True:
            self.immortal = False

    def startPlayer(self):
        self.rect.center = CENTER_POSITION
        self.movement = Direction()
        self.ageInPosition = 0
        self.timeAliveInFrames = 0
        self.immortal = True
        self.movingForward = False
        self.spacePressed = False
        self.playerAlive = True
        self.projectiles = []

    def draw(self, surface):
        if self.immortal == True and (self.timeAliveInFrames % FPS) < FPS/4:
            return
        if not self.movingForward:
            surface.blit(pygame.transform.rotate(self.image, self.movement.degree), self.rect)
        else:
            surface.blit(pygame.transform.rotate(self.imageBoosting, self.movement.degree), self.rect)

        self.drawProjectiles(surface)
    
    def drawProjectiles(self, surface):
        for projectile in self.projectiles:
            projectile.draw(surface)
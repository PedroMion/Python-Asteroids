import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 24
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SPACESHIP_SIZE_IN_PIXELS = 15
PROJECTILE_SIZE_IN_PIXELS = 3
MAX_SPEED = 15
MIN_SPEED = 5
DEFAULT_DIRECTION = pygame.Vector2(0, -1)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FramePerSec = pygame.time.Clock()

pygame.display.set_caption("Asteroids")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Spaceship.png")
        self.imageBoosting = pygame.image.load("./images/Spaceship_turbo.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.direction = DEFAULT_DIRECTION
        self.speed = MIN_SPEED
        self.degree = 0
        self.movingForward = False
        self.projectiles = []

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.handleKeyPress(pressed_keys)
        self.updateAllProjectiles()

        self.move()
    
    def move(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)

    def handleKeyPress(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.moveForward()
        else:
            self.decreaseSpeed()

        if not self.movingForward:
            if pressed_keys[K_LEFT]:
                self.rotateLeft()
            if pressed_keys[K_RIGHT]:
                self.rotateRight()

        if pressed_keys[K_SPACE]:
            self.newProjectile()

    def moveForward(self):
        self.movingForward = True
        if(self.direction == DEFAULT_DIRECTION.rotate(self.degree)):
            self.increaseSpeed()
        else:
            self.speed = MIN_SPEED
            self.direction = DEFAULT_DIRECTION.rotate(self.degree * (-1))

    def increaseSpeed(self):
        if(self.speed <= MAX_SPEED):
            self.speed += (MAX_SPEED - MIN_SPEED) / (2 * FPS)
    
    def decreaseSpeed(self):
        self.movingForward = False
        if(self.speed >= MIN_SPEED):
            self.speed -= (MAX_SPEED - MIN_SPEED) / (2 * FPS)
    
    def rotateLeft(self):
        self.degree = (self.degree + 15) % 360
    
    def rotateRight(self):
        self.degree = (self.degree - 15) % 360

    def newProjectile(self):
        currentDirection = DEFAULT_DIRECTION.rotate(-self.degree)
        projectile = Projectile(currentDirection, self.rect.center, self.degree)

        self.projectiles.append(projectile)

    def updateAllProjectiles(self):
        for projectile in self.projectiles:
            projectile.update([])
            if(projectile.collided):
                self.projectiles.remove(projectile)
                del projectile

    def draw(self, surface):
        if not self.movingForward:
            surface.blit(pygame.transform.rotate(self.image, self.degree), self.rect)
        else:
            surface.blit(pygame.transform.rotate(self.imageBoosting, self.degree), self.rect)

        self.drawProjectiles(surface)
    
    def drawProjectiles(self, surface):
        for projectile in self.projectiles:
            projectile.draw(surface)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, direction, currentPosition, degree):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load("./images/Projectile.png"), degree)
        self.rect = self.image.get_rect()
        self.rect.center = currentPosition
        self.direction = direction
        self.collided = False

    def update(self, meteorList):
        self.moveForward()
        self.checkColision(meteorList)
        self.checkBorderHit()

    def moveForward(self):
        self.rect.move_ip(self.direction[0] * MAX_SPEED, self.direction[1] * MAX_SPEED)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def checkColision(self, meteorList):
        for meteor in meteorList:
            collide = self.rect.colliderect(meteor.rect)
            if collide:
                meteor.destroy()
                self.collided = True
    
    def checkBorderHit(self):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH or self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.collided = True


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
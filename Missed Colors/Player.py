import pygame
from pygame.locals import *
from pygame import mixer
from boxCollision import boxCollision

#-Ignorar-esto,-lo-uso-pa-hacer-test-de-codigo---
mixer.init()
walk = mixer.Sound('sounds//walk.wav')
alert=mixer.Sound('sounds//jump.wav')
#------------------------------------------------

class Player:

    clashManager = boxCollision()
    sprite = pygame.sprite.Sprite()

    deltaX = 0.0
    deltaY = 0.0

    walking = bool()
    still = bool()


    # Constructor
    def _init_(self, x = 300, y = 400):
        self.deltaX = 0
        self.X = x
        self.Y = y
        self.initSpriteData()


    # Setea el sprite con su imagen y rectangulo
    def initSpriteData(self):
        surface = pygame.display.get_surface()
        self.sprite.image = pygame.image.load("sprites//blue.png").convert()
        width = self.sprite.image.get_width()
        height = self.sprite.image.get_height()
        self.sprite.image = pygame.transform.scale(self.sprite.image, (width,height)) 
        self.sprite.rect = pygame.Rect((self.X, self.Y), (width,height))
        

    # Metodo que updatea valores de instancia
    def update(self, elapsedTime, group):      
        # Recibe el input
        pressedKey = pygame.key.get_pressed()

        if pressedKey[K_RIGHT]:
            self.walk(group, 20)
        if pressedKey[K_LEFT]:
            self.walk(group, -20)
        if not pressedKey[K_LEFT] and not pressedKey[K_RIGHT]:
            self.walk(group,0)

        # Una vez definidos deltaX y deltaY, los asigna a sus valores posicion
        self.X += self.deltaX
        self.Y += self.deltaY

        # Al terminar de hacer update, deja listo el rectangulo con los nuevos valores
        self.sprite.rect = pygame.Rect((self.X, self.Y), (self.sprite.rect.width, self.sprite.rect.height))
        

    # Dibuja player en pantalla
    def render(self):
        surface = pygame.display.get_surface()
        surface.blit(self.sprite.image, self.sprite.rect)


    # Metodo de caminata (incompleto, A medida que avancemos le vamos agregando cosas)
    def walk(self, group, xAdvance):

        clashed = self.clashManager.CheckCollision(self.sprite, group, self.X + xAdvance, self.Y)

        if not clashed:
            self.deltaX = xAdvance
        else:
            # choca llendo a la derecha (calcula deltaX exacto para no quedar intersectando bloque)
            if xAdvance > 0:
                rightWallX = self.clashManager.leftX - (self.sprite.rect.width)
                self.deltaX = rightWallX - self.X
            # choca llendo hacia la izquierda (calcula deltaX exacto para no quedar intersectando bloque)
            elif xAdvance < 0:
                leftWallX = self.clashManager.rightX 
                self.deltaX = leftWallX - self.X
            
        

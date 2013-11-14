import pygame
from pygame.locals import *

class boxCollision:

    def _init_(self):
        self.bottomY = 0
        self.topY = 0
        self.rightX = 0
        self.leftX = 0
    
    # Chequea Colision con grupo. Si la hay, investiga de que direccion se dio. Una vez hecho esto, devuelve un valor
    def CheckCollision(self, player, group, x1, y1):

        # Crea sprite en posicion a la que se quiere mover el player
        newPos = pygame.Rect(x1, y1, player.rect.width, player.rect.height)
        playerMoved = pygame.sprite.Sprite()
        playerMoved.rect = newPos

        # Crea una lista con los sprites que colisionan contra el player
        spriteList = pygame.sprite.spritecollide(playerMoved, group, False)

        # El seteo de valores va a servir mas adelante para establecer la posicion despues del choque (para que no haya interseccion)
        if len(spriteList) >= 1:
            rect = spriteList[0].rect
            self.topY = rect.top
            self.bottomY = rect.top + rect.height
            self.rightX = rect.left + rect.width
            self.leftX = rect.left
            return True
        else:
            return False

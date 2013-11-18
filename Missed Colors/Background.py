import pygame
from pygame.locals import *

class Background:

    # crea el grupo y se lo da al metodo spriteinit pa que lo llene
    def _init_(self):
        self.group = pygame.sprite.Group()
        self.spritesInit(self.group)

    def update(self, elapsedTime):
        #self.group.update()
        pass

    def render(self):
        surface = pygame.display.get_surface()
        self.group.draw(surface)

    # Metodo temporal mientras no tengamos el editor de niveles. Aqui es donde
    # tienes que crear los bloques que quieras usar pa probar las colisiones,
    # gravedad, salto, etc.
    def spritesInit(self, group):
        image = pygame.image.load("sprites//brick.png").convert()
        width = image.get_width()
        height = image.get_height()

        brick1 = pygame.sprite.Sprite()
        brick1.image = pygame.transform.scale(image, (width,height)) 
        brick1.rect = pygame.Rect((800, 400), (width,height))

        brick2 = pygame.sprite.Sprite()
        brick2.image = pygame.transform.scale(image, (width,height)) 
        brick2.rect = pygame.Rect((100, 400), (width,height))

        brick3 = pygame.sprite.Sprite()
        brick3.image = pygame.transform.scale(image, (width,height)) 
        brick3.rect = pygame.Rect((200, 500), (width,height))

        brick4 = pygame.sprite.Sprite()
        brick4.image = pygame.transform.scale(image, (width,height)) 
        brick4.rect = pygame.Rect((300, 500), (width,height))

        brick5 = pygame.sprite.Sprite()
        brick5.image = pygame.transform.scale(image, (width,height)) 
        brick5.rect = pygame.Rect((600, 500), (width,height))

        brick6 = pygame.sprite.Sprite()
        brick6.image = pygame.transform.scale(image, (width,height)) 
        brick6.rect = pygame.Rect((700, 500), (width,height))
        
        group.add(brick1, brick2, brick3, brick4, brick5, brick6)


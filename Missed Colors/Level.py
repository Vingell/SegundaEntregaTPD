import pygame
from pygame.locals import *
from Player import Player
from Background import Background


class Level:

    # Para despues
    def _init_(self):
        pass
    
    # Para despues
    def update(self, elapsedTime):
        pass

    # Para despues
    def render(self):
        pass

    pygame.init()
    screenSize = (1280,720)
    screen = pygame.display.set_mode(screenSize, 0, 32)
    pygame.display.set_caption("Missed Colors")

    # Se llama a init porque por alguna razon no lo hace automatico al crear la instancia
    player = Player()
    player._init_()
    background = Background()
    background._init_()

    # Para calcular el tiempo
    clock = pygame.time.Clock()

    while True:

        # Calcula el tiempo que ha pasado entre cada frame (en segundos)
        elapsedTime = clock.tick(30) / 1000.0

        # Eventos (por ahora solo para cerrar ventana)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Update de instancias importantes
        player.update(elapsedTime, background.group)
        background.update(elapsedTime)

        # fondo blanco
        screen.fill((255, 255, 255))
        
        #render de instancias importantes
        player.render()
        background.render()

        pygame.display.update()

    

        

    

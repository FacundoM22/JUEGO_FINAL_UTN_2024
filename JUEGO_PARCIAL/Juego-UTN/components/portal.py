import pygame
from settings.auxiliar import *
from settings.constants import DEBUG


class Portal:
    
    def __init__(self, x, y, w, h, type):
        # Cargar imagen con ruta absoluta
        ruta_imagen = get_ruta_absoluta("../../resources/objects/Portal.png")
        self.image = pygame.image.load(ruta_imagen)

        # Escalar imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (w, h))

        # Definir el rectángulo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, GREEN, self.rect)

        screen.blit(self.image, self.rect)

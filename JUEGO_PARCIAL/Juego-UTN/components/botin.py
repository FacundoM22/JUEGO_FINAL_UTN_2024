import pygame
from settings.auxiliar import *
from settings.constants import DEBUG

class Botin:
    def __init__(self, x, y, w, h, type):
        # Carga la imagen usando ruta absoluta
        ruta_imagen = get_ruta_absoluta("../../resources/objects/Portal.png")
        self.image = pygame.image.load(ruta_imagen)

        # Escala la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (w, h))

        # Define el rectángulo del botín
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

        # Rectángulo de colisión (opcional, en caso de que lo necesites)
        self.rect_botin_collition = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, self.rect.height
        )

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, GREEN, self.rect_botin_collition)

        screen.blit(self.image, self.rect)

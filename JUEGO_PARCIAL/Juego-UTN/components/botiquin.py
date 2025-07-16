import pygame
from settings.auxiliar import *
from settings.constants import DEBUG

class Botiquin:
    
    def __init__(self, x, y, w, h, type=0):
        # Cargar imagen con ruta absoluta
        ruta_imagen = get_ruta_absoluta("../../resources/objects/Corazon.png")
        self.image = pygame.image.load(ruta_imagen)
        
        # Escalar imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (w, h))
        
        # Definir el rectángulo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = self.rect

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, GREEN, self.rect)

        screen.blit(self.image, self.rect)

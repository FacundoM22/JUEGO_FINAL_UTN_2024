import pygame
from settings.auxiliar import *
from settings.constants import DEBUG


class Trampa:
    def __init__(self, x, y, w, h, type):
        # Obtener ruta absoluta a la imagen de la trampa
        ruta_imagen = get_ruta_absoluta("../../resources/objects/trampa.png")
        self.image = pygame.image.load(ruta_imagen)

        # Escala la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (w, h))

        # Define el rectángulo visual de la trampa
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Define un rectángulo de colisión más pequeño
        self.collision_rect = pygame.Rect(
            self.rect.x + 10,  # Ajusta el desplazamiento horizontal
            self.rect.y + 10,  # Ajusta el desplazamiento vertical
            self.rect.width - 20,  # Ajusta el ancho
            self.rect.height - 20  # Ajusta la altura
        )

        self.type = type

    def draw(self, screen):
        if DEBUG:
            # Dibujar el rectángulo de colisión verde
            pygame.draw.rect(screen, GREEN, self.collision_rect)

        # Dibujar la imagen de la trampa
        screen.blit(self.image, self.rect)

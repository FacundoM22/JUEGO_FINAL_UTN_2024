import pygame
from auxiliar import *




class Portal:
    
    def __init__(self, x, y, w, h, type):
            # Carga una imagen PNG directamente
            self.image = pygame.image.load(r"resources\objects\Portal.png")  # Cambia a la ruta correcta de tu archivo PNG

            # Escala la imagen al tamaño deseado
            self.image = pygame.transform.scale(self.image, (w, h))

            # Define el rectángulo de la trampa
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.type = type

        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect)

        screen.blit(self.image,self.rect)

        
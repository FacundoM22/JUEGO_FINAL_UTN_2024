import pygame
import os
from settings.constants import ALTO_VENTANA, ANCHO_VENTANA
from settings.utils import get_ruta_absoluta  # O el módulo donde esté la función

def get_fuente(size=20):
    # Usamos get_ruta_absoluta para la ruta de la fuente
    ruta_fuente = get_ruta_absoluta(os.path.join("..", "assets", "fonts", "PressStart2P-Regular.ttf"))
    return pygame.font.Font(ruta_fuente, size)

def cargar_background():
   ruta_bg = get_ruta_absoluta(os.path.join("..", "..", "resources", "background", "vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640", "backgroundMenu.jpg"))
   return pygame.image.load(ruta_bg)


Background = pygame.transform.scale(cargar_background(), (ANCHO_VENTANA, ALTO_VENTANA))

clock = pygame.time.Clock()

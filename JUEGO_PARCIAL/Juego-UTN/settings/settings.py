import pygame
import os

def get_fuente(size=20):
    base_path = os.path.dirname(__file__)  # Ruta de settings.py
    ruta_fuente = os.path.join(base_path, "..", "assets", "fonts", "PressStart2P-Regular.ttf")
    ruta_fuente = os.path.normpath(ruta_fuente)  # Normaliza los .. y separadores
    return pygame.font.Font(ruta_fuente, size)
def cargar_background():
    return pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\background\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640\backgroundMenu.png")

clock = pygame.time.Clock()

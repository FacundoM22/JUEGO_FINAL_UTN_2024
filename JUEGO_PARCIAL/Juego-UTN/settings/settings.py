import pygame

def get_fuente():
    return pygame.font.SysFont("Cambria", 31)

def cargar_background():
    return pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\background\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640\backgroundMenu.png")

clock = pygame.time.Clock()

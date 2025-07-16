import pygame
from settings.ui_helpers import get_ruta_absoluta



ANCHO_VENTANA = 1600
ALTO_VENTANA = 900
FPS = 60

DIRECTION_L = 0
DIRECTION_R = 1
DIRECTION_UP = -1  # Movimiento hacia arriba en el eje Y (en Pygame, valores negativos suben)
DIRECTION_DOWN = 1  # Opcional: Movimiento hacia abajo en el eje Y

pausa = False

JSON_PATH = get_ruta_absoluta(r'..\json.json')  # Ajustá la ruta relativa desde este archivo





RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
FUCHSIA = (255, 0, 255)


GROUND_RECT_H = 7
GROUND_LEVEL = 630

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip=False, step=1, scale_factor=1):
        lista = []
        surface_imagen = pygame.image.load(path).convert_alpha()
        fotograma_ancho = int(surface_imagen.get_width() / columnas)
        fotograma_alto = int(surface_imagen.get_height() / filas)
        
        for fila in range(filas):
            for columna in range(0, columnas, step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface((x, y, fotograma_ancho, fotograma_alto))
                
                # Voltear el frame si flip=True
                if flip:
                    surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)
                
                # Escalar el frame si scale_factor != 1
                if scale_factor != 1:
                    new_width = int(fotograma_ancho * scale_factor)
                    new_height = int(fotograma_alto * scale_factor)
                    surface_fotograma = pygame.transform.scale(surface_fotograma, (new_width, new_height))
                
                lista.append(surface_fotograma)
        
        return lista

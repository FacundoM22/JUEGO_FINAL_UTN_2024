import pygame
from settings.auxiliar import *
from components.button import *
from settings.settings import get_fuente

# Cargá la imagen del botón UNA vez y la reutilizás
IMAGEN_BOTON = pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\button.png")
IMAGEN_BOTON = pygame.transform.scale(IMAGEN_BOTON, (270, 100))  # Nuevo tamaño (ancho, alto)



def render_titulo_con_efecto(screen, texto, pos_y, alpha, fuente=None, color=(255, 255, 255)):

    if fuente is None:
        fuente = get_fuente()
    
    texto_surface = fuente.render(texto, True, color)
    texto_surface.set_alpha(alpha)
    rect = texto_surface.get_rect(center=(ANCHO_VENTANA // 2, pos_y))
    screen.blit(texto_surface, rect)
    return rect  # Devuelve el rectángulo por si necesitas detectar clicks

def crear_boton_salir(pos):
    """Crea y devuelve el botón 'SALIR'."""
    return Button(
        image=IMAGEN_BOTON,
        pos=pos,
        text_input="SALIR",
        font = get_fuente(),
        base_color="#000000",
        hovering_color="#5a0e54"
    )

def crear_botones(contexto, texto_opciones="MUSIC ON", fuente=None):
    """Crea botones para distintos contextos con posiciones ordenadas."""
    botones = {}
    espacio_entre = 100
    y_inicial = 300
    x_centro = ANCHO_VENTANA / 2

    if fuente is None:
        fuente = get_fuente()

    if contexto == "menu_principal":
        textos = ["JUGAR", texto_opciones, "SALIR"]
        claves = ["jugar", "opciones", "salir"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            if clave == "salir":
                botones[clave] = crear_boton_salir(pos)
            else:
                botones[clave] = Button(
                    image=IMAGEN_BOTON,
                    pos=pos,
                    text_input=texto,
                    font=fuente,
                    base_color="#000000",
                    hovering_color="#5a0e54"
                )

    elif contexto == "seleccionar_nivel":
        textos = ["NIVEL 1", "NIVEL 2", "NIVEL 3"]
        claves = ["nivel1", "nivel2", "nivel3"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            botones[clave] = Button(
                image=IMAGEN_BOTON,
                pos=pos,
                text_input=texto,
                font=fuente,
                base_color="#000000",
                hovering_color="#5a0e54"
            )

    elif contexto == "ranking":
        textos = ["MENU PRINCIPAL", "SALIR"]
        claves = ["menu_principal", "salir"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            botones[clave] = Button(
                image=IMAGEN_BOTON,
                pos=pos,
                text_input=texto,
                font=fuente,
                base_color="#000000",
                hovering_color="#5a0e54"
            )

    elif contexto == "pausa":
        textos = ["SELECCIONAR NIVEL", texto_opciones, "SALIR"]
        claves = ["continuar", "opciones", "salir"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            if clave == "salir":
                botones[clave] = crear_boton_salir(pos)
            else:
                botones[clave] = Button(
                    image=IMAGEN_BOTON,
                    pos=pos,
                    text_input=texto,
                    font=fuente,
                    base_color="#000000",
                    hovering_color="#5a0e54"
                )

    return botones

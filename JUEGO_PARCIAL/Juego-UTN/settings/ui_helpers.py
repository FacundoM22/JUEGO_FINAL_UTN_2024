import pygame
from settings.auxiliar import *
from components.button import *

# Cargá la imagen del botón UNA vez y la reutilizás
IMAGEN_BOTON = pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\button.png")

def crear_boton_salir(pos, fuente):
    """Crea y devuelve el botón 'SALIR'."""
    return Button(
        image=IMAGEN_BOTON,
        pos=pos,
        text_input="SALIR",
        font=fuente,
        base_color="#a9a9a9",
        hovering_color="#7faaff"
    )

def crear_botones(contexto, texto_opciones="MUSIC ON", fuente=None):
    """Crea botones para distintos contextos con posiciones ordenadas."""
    botones = {}
    espacio_entre = 100
    y_inicial = 300
    x_centro = ANCHO_VENTANA / 2

    if fuente is None:
        fuente = pygame.font.SysFont("Cambria", 31)

    if contexto == "menu_principal":
        textos = ["JUGAR", texto_opciones, "SALIR"]
        claves = ["jugar", "opciones", "salir"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            if clave == "salir":
                botones[clave] = crear_boton_salir(pos, fuente)
            else:
                botones[clave] = Button(
                    image=IMAGEN_BOTON,
                    pos=pos,
                    text_input=texto,
                    font=fuente,
                    base_color="#a9a9a9",
                    hovering_color="#7faaff"
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
                base_color="#a9a9a9",
                hovering_color="#7faaff"
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
                base_color="#a9a9a9",
                hovering_color="#7faaff"
            )

    elif contexto == "pausa":
        textos = ["SELECCIONAR NIVEL", texto_opciones, "SALIR"]
        claves = ["continuar", "opciones", "salir"]
        for i, (clave, texto) in enumerate(zip(claves, textos)):
            pos = (x_centro, y_inicial + i * espacio_entre)
            if clave == "salir":
                botones[clave] = crear_boton_salir(pos, fuente)
            else:
                botones[clave] = Button(
                    image=IMAGEN_BOTON,
                    pos=pos,
                    text_input=texto,
                    font=fuente,
                    base_color="#a9a9a9",
                    hovering_color="#7faaff"
                )

    return botones

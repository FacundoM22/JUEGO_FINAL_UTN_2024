# ui_helpers.py
import pygame
from components.button import Button
from settings.auxiliar import *

def crear_boton_salir(pos, fuente):
    """Crea y devuelve el botón 'SALIR'."""
    return Button(
        image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
        pos=pos,
        text_input="SALIR",
        font=fuente,
        base_color="#d7fcd4",
        hovering_color="Black"
    )

def crear_botones(contexto, texto_opciones="MUSIC ON"):
    """Crea botones para distintos contextos."""
    botones = {}
    if contexto == "menu_principal":
        botones = {
            "jugar": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 350),
                text_input="JUGAR",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "opciones": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 500),
                text_input=texto_opciones,
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "salir": crear_boton_salir((ANCHO_VENTANA / 2, 650), pygame.font.SysFont("Cambria", 31))
        }
    elif contexto == "seleccionar_nivel":
        botones = {
            "nivel1": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 250),
                text_input="NIVEL 1",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "nivel2": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 400),
                text_input="NIVEL 2",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "nivel3": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 550),
                text_input="NIVEL 3",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            )
        }
    elif contexto == "ranking":
        botones = {
            "menu_principal": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 650),
                text_input="MENU PRINCIPAL",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "salir": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 750),
                text_input="SALIR",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            )
        }
    elif contexto == "pausa":
        botones = {
            "continuar": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 300),
                text_input="SELECCIONAR NIVEL",
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "opciones": Button(
                image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/arcade_start_button_no_text.png"),
                pos=(ANCHO_VENTANA / 2, 400),
                text_input=texto_opciones,
                font=pygame.font.SysFont("Cambria", 31),
                base_color="#d7fcd4",
                hovering_color="Black"
            ),
            "salir": crear_boton_salir((ANCHO_VENTANA / 2, 500), pygame.font.SysFont("Cambria", 31))
        }

    return botones

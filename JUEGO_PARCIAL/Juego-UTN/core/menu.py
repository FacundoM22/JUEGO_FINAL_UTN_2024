import pygame
import sys
from core.nivel_selector import *
from tkinter import *
from settings.auxiliar import *
from settings.settings import *
from settings.ui_helpers import *

def main_menu():
    fuente = get_fuente()  # Crear fuente acá, dentro de la función
    global username, music
    music = True
    texto_opciones = "MUSIC ON" if music else "MUSIC OFF"
    botones = crear_botones("menu_principal", texto_opciones)  # Crear botones centralizados

    # Configuración para el input del username
    input_rect = pygame.Rect((ANCHO_VENTANA // 2 - 200), 750, 400, 50)
    color = pygame.Color('Black')  # Color del rectángulo de input
    active = False  # Estado de edición del input
    username = ""

    while True:
        screen.blit(Background, (0, 0))  # Dibujar el fondo
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Título del menú
        MENU_TEXT = fuente.render("MENU PRINCIPAL", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA / 2), 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        # Mostrar input para el nombre de usuario
        username_text = fuente.render("Nombre de usuario: ", True, "Black")
        screen.blit(username_text, (input_rect.x - 280, input_rect.y + 1))
        pygame.draw.rect(screen, color, input_rect, 2)  # Rectángulo del input
        user_surface = fuente.render(username, True, "White")
        screen.blit(user_surface, (input_rect.x + 20, input_rect.y + 10))

        # Validación del nombre de usuario
        error_message = ""
        if len(username.strip()) < 5:
            error_message = "El nombre debe tener al menos 5 caracteres."
        elif len(username.strip()) > 20:
            error_message = "El nombre no puede superar los 20 caracteres."
        elif username.strip() == "":
            error_message = "El campo no puede estar vacío."

        if error_message:
            error_surface = fuente.render(error_message, True, "Red")
            screen.blit(error_surface, (input_rect.x - 150, input_rect.y + 100))

        # Dibujar botones
        for button in botones.values():
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        # Eventos del menú principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):  # Activar o desactivar input
                    active = not active
                else:
                    active = False

                if botones["jugar"].checkForInput(MENU_MOUSE_POS):
                    if not error_message:  # Solo proceder si no hay errores
                        seleccionar_nivel()
                if botones["opciones"].checkForInput(MENU_MOUSE_POS):
                    music = not music
                    botones["opciones"].text_input = "MUSIC ON" if music else "MUSIC OFF"
                if botones["salir"].checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:  # Manejar edición del input solo si está activo
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif len(username) < 20:  # Limitar longitud del nombre de usuario
                        username += event.unicode

        # Cambiar color del borde si el input está activo
        color = pygame.Color('Blue') if active else pygame.Color('Black')

        # Actualizar pantalla
        pygame.display.update()
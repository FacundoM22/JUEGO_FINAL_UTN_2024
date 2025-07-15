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

    efecto_titulo = EfectoAlpha(velocidad=3)
    
    while True:

        alpha = efecto_titulo.update()

        

        screen.blit(Background, (0, 0))  # Dibujar el fondo
        MENU_MOUSE_POS = pygame.mouse.get_pos()


    # Título del menú (con alpha para efecto fade)
        render_titulo_con_efecto(screen,"MENU PRINCIPAL",100,alpha)

        # Texto de la etiqueta "Nombre de usuario" con fondo
        username_text = fuente.render("Nombre de usuario: ", True, (255, 255, 255))

        padding_x = 10
        padding_y = 6

        bg_width = username_text.get_width() + 2 * padding_x
        bg_height = username_text.get_height() + 2 * padding_y
        label_bg = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        label_bg.fill((0, 0, 0, 180))

        label_x = input_rect.x - bg_width - 10
        label_y = input_rect.y + (input_rect.height - bg_height) // 2

        screen.blit(label_bg, (label_x, label_y))

        text_x = label_x + padding_x
        text_y = label_y + padding_y
        screen.blit(username_text, (text_x, text_y))

        # Ahora sí: dibujar la caja donde se escribe y el texto tipeado
        pygame.draw.rect(screen, color, input_rect, 2)
        fondo_caja = pygame.Surface((input_rect.width,input_rect.height), pygame.SRCALPHA)
        fondo_caja.fill((0,0,0, 180))
        screen.blit(fondo_caja,input_rect)

        user_surface = fuente.render(username, True, "White")
        screen.blit(user_surface, (input_rect.x + 20, input_rect.y + 10))

        


       # Validación del nombre de usuario
        error_message = ""
        username_stripped = username.strip()

        if username_stripped == "":
            error_message = "El campo no puede estar vacío."
        elif len(username_stripped) < 5:
            error_message = "El nombre debe tener al menos 5 caracteres."
        elif len(username_stripped) > 20:
            error_message = "El nombre no puede superar los 20 caracteres."

        if error_message:
            error_surface = fuente.render(error_message, True, (255, 0, 0))  # Texto rojo

            # Padding para el fondo del error
            padding_x = 10
            padding_y = 6

            # Crear fondo del tamaño del texto + padding
            bg_width = error_surface.get_width() + 2 * padding_x
            bg_height = error_surface.get_height() + 2 * padding_y
            error_bg = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
            error_bg.fill((0, 0, 0, 180))  # Fondo negro translúcido

            # Posición del fondo justo debajo del input (con margen)
            error_x = input_rect.x - 10
            error_y = input_rect.y + input_rect.height + 15  # 15 px debajo del input

            # Dibujar fondo y texto con padding
            screen.blit(error_bg, (error_x, error_y))
            screen.blit(error_surface, (error_x + padding_x, error_y + padding_y))

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
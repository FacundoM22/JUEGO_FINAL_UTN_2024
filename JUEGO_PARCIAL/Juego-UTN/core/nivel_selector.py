import pygame
import sys
from tkinter import *
from settings.settings import *
from settings.auxiliar import *
from settings.ui_helpers import crear_botones
from settings.settings import get_fuente


Background = cargar_background()

def seleccionar_nivel():
    fuente = get_fuente()
    from core.game_loop import play
    botones = crear_botones("seleccionar_nivel")

    while True:
        screen.blit(Background, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("SELECCIONA EL NIVEL:", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA / 2), 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in botones.values():
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["nivel1"].checkForInput(MENU_MOUSE_POS):
                    play(False, 1)
                if botones["nivel2"].checkForInput(MENU_MOUSE_POS):
                    play(False, 2)
                if botones["nivel3"].checkForInput(MENU_MOUSE_POS):
                    play(False, 3)

        pygame.display.update()


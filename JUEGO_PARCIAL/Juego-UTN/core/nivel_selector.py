import pygame
import sys
from managers.sound_manager import *
from tkinter import *
from settings.settings import *
from settings.auxiliar import *
from settings.ui_helpers import crear_botones, render_titulo_con_efecto
from settings.settings import get_fuente
from settings.efects import EfectoAlpha



def seleccionar_nivel(callback_volver_menu= None):
    
    fuente = get_fuente()
    from core.game_loop import play

    def seleccionar_nivel(callback_volver_menu=None):
         stop_music()  # detiene la música para que no suene acá
    # resto del código...
    botones = crear_botones("seleccionar_nivel")
    efecto_titulo = EfectoAlpha(velocidad=3)
    while True:
        screen.blit(Background, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        alpha = efecto_titulo.update()
        render_titulo_con_efecto(screen,"SELECCIONAR NIVEL", 100, alpha)

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
                if botones.get("menu_principal") and botones["menu_principal"].checkForInput(MENU_MOUSE_POS):
                    if callback_volver_menu:
                        callback_volver_menu()
                    
                    
                if botones["salir"].checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


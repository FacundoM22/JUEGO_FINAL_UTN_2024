import pygame
import sys
from core.nivel_selector import *
from tkinter import *
from settings.auxiliar import *
#from plataforma import Platform
from settings.settings import get_fuente, cargar_background, clock


fuente = get_fuente()
Background = cargar_background()

def game_over():
    fuente = get_fuente()  
    pygame.mixer.music.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\Sounds\gameOver.ogg")
    pygame.mixer.music.set_volume(0.25)  # Ajusta el volumen según sea necesario
    pygame.mixer.music.play(-1)  
    while True:
        screen.blit(Background,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("GAME OVER", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 300))

        PLAY_BUTTON = Button(image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\arcade_start_button_no_text.png"), pos=((ANCHO_VENTANA / 2), 550), 
                             text_input="JUGAR", font=fuente, base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\arcade_start_button_no_text.png"), pos=((ANCHO_VENTANA / 2), 650), 
                             text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black")


        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    seleccionar_nivel()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

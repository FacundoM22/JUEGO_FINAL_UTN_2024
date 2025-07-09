from settings.settings import *
from settings.auxiliar import *
from components.button import Button
import sys


Background = cargar_background()

def mostar_ranking():
    fuente = get_fuente()
    while True:
        screen.blit(Background, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("RANKING:", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA / 2), 100))

        QUIT_BUTTON = Button(
            image=pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\arcade_start_button_no_text.png"), 
            pos=((ANCHO_VENTANA / 2), 550), 
            text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black"
        )

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
          
        pygame.display.update()

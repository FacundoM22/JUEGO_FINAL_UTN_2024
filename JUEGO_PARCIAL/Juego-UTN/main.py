import pygame
import sys
from tkinter import *
from bulletmanager import *
from player import Player
from enemigo import Enemigo
#from plataforma import Platform
from auxiliar import *
from button import *
from portal import Portal
from trampa import Trampa
from fuctions import *
from botin import Botin
from botiquin import Botiquin
from db_manager import *
from ui_helpers import  crear_botones
lista_plataformas = []
username = ""


clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
init_db()

fuente = pygame.font.SysFont("Cambria",31)

Background = pygame.image.load(r"resources\background\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640\backgroundMenu.png")


def mostar_ranking():
    while True:
        screen.blit(Background,(0,0))
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("RANKING:", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA/2), 100))

        QUIT_BUTTON = Button(image=pygame.image.load(r"resources\arcade_start_button_no_text.png"), pos=((ANCHO_VENTANA/2), 550), 
                            text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black")

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




def seleccionar_nivel():
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



def main_menu():
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



def play(pausa, level):
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    botones = crear_botones("pausa")
    pygame.mixer.music.load(r"resources\Sounds\relaxing-video-game-music-for-archeologists-and-explorers-_-_Fv2SmiCyTzI_.ogg")
    pygame.mixer.music.set_volume(.25)
    global username
    global music
    paused = False  # Estado de pausa

    player_1 = Player(x=0, y=100, speed_walk=4, speed_run=8, gravity=8, jump_power=90, frame_rate_ms=80, move_rate_ms=10, jump_height=150, energia=100, bullets=100, healt=100, live=1)
    lista = load_json_info(JSON_PATH)
    lista_balas = []
    lista_botines = []
    bulletmanager_1 = BulletManager(player_1.bullets, 10000)
    lista_balas = bulletmanager_1.balas_disparadas

    if music:
        pygame.mixer.music.play(loops=1)
    else:
        pygame.mixer.music.stop()

    lista_players = []

    if level == 1:
        imagen_fondo = pygame.image.load(r"resources\scenes\nivel1\45859.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        lista_players.append(player_1)
        lista_trampas = tomar_objetos(lista['nivel1']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel1']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel1']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel1']['enemy'])
    elif level == 2:
        imagen_fondo = pygame.image.load(r"resources\scenes\nivel2\45865.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        lista_players.append(player_1)
        lista_trampas = tomar_objetos(lista['nivel2']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel2']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel2']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel2']['enemy'])
    elif level == 3:
        imagen_fondo = pygame.image.load(r"resources/background/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        lista_players.append(player_1)
        lista_enemigos = tomar_enemigo(lista['nivel3']['enemy'])

    lista_characters = lista_players + lista_enemigos

    pygame.display.set_caption("Jugando")
    while RUNNING:
        keys = pygame.key.get_pressed()  # Obtén el estado actual de las teclas

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Alternar estado de pausa
                    paused = not paused

        if paused:
            while paused:
                screen.blit(imagen_fondo, (0, 0))  # Fondo del juego
                pause_text = fuente.render("PAUSA - Presiona ESC para continuar", True, "Black")
                screen.blit(pause_text, (ANCHO_VENTANA // 2 - pause_text.get_width() // 2, 100))  # Centrar texto

                # Dibuja los botones
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                for button in botones.values():
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            paused = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botones["continuar"].checkForInput(MENU_MOUSE_POS):
                           seleccionar_nivel()
                        if botones["opciones"].checkForInput(MENU_MOUSE_POS):
                            music = not music
                            if music:
                                pygame.mixer.music.unpause()  # Reanuda la música
                                botones["opciones"].text_input = "MUSIC ON"
                                # Ajustar el volumen de los sonidos del jugador
                                for player in lista_players:  # Asegúrate de que `lista_players` esté inicializada
                                    player.set_sound_volume(music)

                                bulletmanager_1.set_sound_volume(music)
                            else:
                                pygame.mixer.music.pause()  # Pausa la música
                                botones["opciones"].text_input = "MUSIC OFF"
                                                        # Ajustar el volumen de los sonidos del jugador
                            for player in lista_players:  # Asegúrate de que `lista_players` esté inicializada
                                player.set_sound_volume(music)
                            
                            for enemigo in lista_enemigos:
                                enemigo.set_sound_volume(music)

                            bulletmanager_1.set_sound_volume(music)

                        if botones["salir"].checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()

                pygame.display.update()




            pygame.display.flip()
            continue  # Salta el resto de la lógica mientras está en pausa

        # Lógica del disparo
        if keys[pygame.K_x]:  # Disparar con tecla X
            bulletmanager_1.shoot(player_1.rect.x, player_1.rect.y + 20, player_1.direction, True)
        elif keys[pygame.K_r]:  # Recargar con tecla R
            bulletmanager_1.reload()

        # Lógica del juego (intacta)
        delta_ms = clock.tick(FPS)

        texto_energia = fuente.render("Energia: {0}%".format(player_1.energia), True, "White")
        texto_balas = fuente.render("Balas: {0}".format(len(bulletmanager_1.balas_player)), True, "White")
        texto_vida = fuente.render("Vida: {0}".format((player_1.health)), True, "White")

        screen.blit(imagen_fondo, imagen_fondo.get_rect())


        if player_1.is_dead():
            pygame.mixer.music.stop()
            game_over()
            return  # Salir del bucle principal

        for portal in lista_portales:
            portal.draw(screen)
            if player_1.rect_character_collition.colliderect(portal.rect):
                # Detener música de fondo
                pygame.mixer.music.stop()

                # Silenciar todos los sonidos del jugador
                for player in lista_players:
                    player.set_sound_volume(False)  # False para silenciar

                # Silenciar los sonidos del BulletManager
                bulletmanager_1.set_sound_volume(False)

                print("¡Ganaste!")
                save_score(username, player_1.health)
                show_ranking()
                return  # Salir del bucle y terminar el nivel


        for trampa in lista_trampas:
            trampa.draw(screen)


        for botiquin in lista_botiquines:
            botiquin.draw(screen)

        for enemigo in lista_enemigos:
            
            enemigo.move_enemy(delta_ms, True, bulletmanager_1)
            enemigo.update(delta_ms, lista_plataformas, lista_enemigos, lista_balas)
            enemigo.draw(screen, lista_enemigos, scale_factor=2.0)

        for player in lista_players:
            player.events(keys)
            player.update(delta_ms, lista_plataformas, lista_balas, lista_players,lista_trampas,lista_botiquines)
            player.draw(screen, lista_players, scale_factor=2.0)

        screen.blit(texto_energia, (30, 30))
        screen.blit(texto_balas, (30, 60))
        screen.blit(texto_vida, (30, 90))

        for bala in bulletmanager_1.balas_disparadas:
            bala.update_bullet(delta_ms, lista_characters, bulletmanager_1.balas_disparadas)  # Pasar listas necesarias
            bala.draw(screen)  # Dibujar la bala en pantalla
            # Verificar colisión con el jugador
            if player_1.rect_character_collition.colliderect(bala.bullet_rect) and not bala.player_bullet:
                player_1.health -= 10  # Reducir salud del jugador
                print(f"¡Jugador recibió daño! Salud restante: {player_1.health}")
                bulletmanager_1.balas_disparadas.remove(bala)  # Eliminar la bala tras la colisión
        pygame.display.flip()





def game_over():
    pygame.mixer.music.load(r"resources\Sounds\gameOver.ogg")
    pygame.mixer.music.set_volume(0.25)  # Ajusta el volumen según sea necesario
    pygame.mixer.music.play(-1)  
    while True:
        screen.blit(Background,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("GAME OVER", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 300))

        PLAY_BUTTON = Button(image=pygame.image.load(r"resources\arcade_start_button_no_text.png"), pos=((ANCHO_VENTANA / 2), 550), 
                             text_input="JUGAR", font=fuente, base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load(r"resources\arcade_start_button_no_text.png"), pos=((ANCHO_VENTANA / 2), 650), 
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


main_menu()
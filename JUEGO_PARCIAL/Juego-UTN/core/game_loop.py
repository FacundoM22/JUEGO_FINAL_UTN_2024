import pygame
import sys
from settings.settings import *
from settings.auxiliar import *
from settings.ui_helpers import crear_botones, get_ruta_absoluta
from components.player import Player
from components.portal import Portal
from components.trampa import Trampa
from components.botiquin import Botiquin
from managers.bulletmanager import BulletManager
from components.fuctions import load_json_info, tomar_objetos, tomar_enemigo
from core.game_over import game_over
from core.game_win import PantallaVictoria
from managers.db_manager import save_score
from settings.settings import get_fuente
from core.nivel_selector import seleccionar_nivel
from settings.constants import RUNNING

pantalla_victoria = PantallaVictoria(screen)
pantalla_victoria.mostrar_ranking()
fuente = get_fuente()

# Defino music como variable global fuera de la función para mantener su estado
music = True
username = ""

def play(pausa, level):
    global music
    global username

    MENU_MOUSE_POS = pygame.mouse.get_pos()
    botones = crear_botones("pausa")

    paused = False

    player_1 = Player(x=0, y=100, speed_walk=4, speed_run=8, gravity=8, jump_power=90,
                      frame_rate_ms=80, move_rate_ms=10, jump_height=150,
                      energia=100, bullets=100, healt=100, live=1)
    lista = load_json_info(JSON_PATH)
    bulletmanager_1 = BulletManager(player_1.bullets, 10000)
    lista_balas = bulletmanager_1.balas_disparadas

    lista_players = []
    lista_trampas = []
    lista_botiquines = []
    lista_portales = []
    lista_enemigos = []
    lista_plataformas = []

    lista_players.append(player_1)

    # Cargar fondo y objetos según nivel
    if level == 1:
        ruta_fondo = get_ruta_absoluta("../../resources/scenes/nivel1/45859.jpg")
        lista_trampas = tomar_objetos(lista['nivel1']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel1']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel1']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel1']['enemy'])
    elif level == 2:
        ruta_fondo = get_ruta_absoluta("../../resources/scenes/nivel2/45865.jpg")
        lista_trampas = tomar_objetos(lista['nivel2']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel2']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel2']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel2']['enemy'])
    elif level == 3:
        ruta_fondo = get_ruta_absoluta("../../resources/scenes/nivel3/45870.jpg")  # Fondo nivel 3 correcto
        lista_trampas = tomar_objetos(lista['nivel3']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel3']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel3']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel3']['enemy'])
    else:
        ruta_fondo = get_ruta_absoluta("../../resources/scenes/nivel1/45859.jpg")  # fallback

    imagen_fondo = pygame.image.load(ruta_fondo)
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    lista_characters = lista_players + lista_enemigos

    pygame.display.set_caption("Jugando")

    while RUNNING:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused

        if paused:
            while paused:
                screen.blit(imagen_fondo, (0, 0))
                pause_text = fuente.render("PAUSA - Presiona ESC para continuar", True, "Black")
                screen.blit(pause_text, (ANCHO_VENTANA // 2 - pause_text.get_width() // 2, 100))

                MENU_MOUSE_POS = pygame.mouse.get_pos()
                for button in botones.values():
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        paused = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botones["continuar"].checkForInput(MENU_MOUSE_POS):
                            seleccionar_nivel()
                            paused = False
                        if botones["opciones"].checkForInput(MENU_MOUSE_POS):
                            music = not music
                            if music:
                                pygame.mixer.music.unpause()
                                botones["opciones"].text_input = "MUSIC ON"
                            else:
                                pygame.mixer.music.pause()
                                botones["opciones"].text_input = "MUSIC OFF"

                            # Actualizar volumen/sonido en jugadores y enemigos
                            for player in lista_players:
                                player.set_sound_volume(music)
                            for enemigo in lista_enemigos:
                                enemigo.set_sound_volume(music)
                            bulletmanager_1.set_sound_volume(music)

                        if botones["salir"].checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()

                pygame.display.update()
            continue  # Saltar resto del loop mientras esté pausado

        # Lógica disparo
        if keys[pygame.K_x]:
            bulletmanager_1.shoot(player_1.rect.x, player_1.rect.y + 20, player_1.direction, True)
        elif keys[pygame.K_r]:
            bulletmanager_1.reload()

        delta_ms = clock.tick(FPS)

        texto_energia = fuente.render(f"Energia: {player_1.energia}%", True, "White")
        texto_balas = fuente.render(f"Balas: {len(bulletmanager_1.balas_player)}", True, "White")
        texto_vida = fuente.render(f"Vida: {player_1.health}", True, "White")

        screen.blit(imagen_fondo, (0, 0))

        if player_1.is_dead():
            pygame.mixer.music.stop()
            game_over()
            return

        for portal in lista_portales:
            portal.draw(screen)
            if player_1.rect_character_collition.colliderect(portal.rect):
                pygame.mixer.music.stop()
                save_score(username, player_1.health)


                player_1.stop_all_sounds()
                
                mostrar_ranking = True
                while mostrar_ranking:
                    for event in pygame.event.get():
                        resultado = pantalla_victoria.manejar_eventos(event)
                        if resultado in ["menu", "salir"] or event.type == pygame.KEYDOWN:
                            mostrar_ranking = False

                    pantalla_victoria.actualizar()
                    pygame.display.update()

                return

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
            player.update(delta_ms, lista_plataformas, lista_balas, lista_players, lista_trampas, lista_botiquines)
            player.draw(screen, lista_players, scale_factor=2.0)

        screen.blit(texto_energia, (30, 30))
        screen.blit(texto_balas, (30, 60))
        screen.blit(texto_vida, (30, 90))

        for bala in bulletmanager_1.balas_disparadas:
            bala.update_bullet(delta_ms, lista_characters, bulletmanager_1.balas_disparadas)
            bala.draw(screen)
            if player_1.rect_character_collition.colliderect(bala.bullet_rect) and not bala.player_bullet:
                player_1.health -= 10
                print(f"¡Jugador recibió daño! Salud restante: {player_1.health}")
                bulletmanager_1.balas_disparadas.remove(bala)

        pygame.display.flip()

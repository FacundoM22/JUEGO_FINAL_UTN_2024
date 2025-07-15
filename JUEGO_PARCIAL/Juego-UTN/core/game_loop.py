import pygame
import sys
from settings.settings import *
from settings.auxiliar import *
from settings.ui_helpers import crear_botones
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


pantalla_victoria = PantallaVictoria(screen)
pantalla_victoria.mostrar_ranking()
fuente = get_fuente()

def play(pausa, level):
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    botones = crear_botones("pausa")
    pygame.mixer.music.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\Sounds\relaxing-video-game-music-for-archeologists-and-explorers-_-_Fv2SmiCyTzI_.ogg")
    pygame.mixer.music.set_volume(.25)
    global username
    global music
    paused = False  # Estado de pausa
    music = True

    player_1 = Player(x=0, y=100, speed_walk=4, speed_run=8, gravity=8, jump_power=90, frame_rate_ms=80, move_rate_ms=10, jump_height=150, energia=100, bullets=100, healt=100, live=1)
    lista = load_json_info(JSON_PATH)
    lista_balas = []
    lista_botines = []
    lista_plataformas = []
    username = ""
    bulletmanager_1 = BulletManager(player_1.bullets, 10000)
    lista_balas = bulletmanager_1.balas_disparadas

    if music:
        pygame.mixer.music.play(loops=1)
    else:
        pygame.mixer.music.stop()

    lista_players = []

    if level == 1:
        imagen_fondo = pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\scenes\nivel1\45859.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        lista_players.append(player_1)
        lista_trampas = tomar_objetos(lista['nivel1']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel1']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel1']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel1']['enemy'])
    elif level == 2:
        imagen_fondo = pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\scenes\nivel2\45865.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        lista_players.append(player_1)
        lista_trampas = tomar_objetos(lista['nivel2']['trampas'], Trampa)
        lista_botiquines = tomar_objetos(lista['nivel2']['botiquines'], Botiquin)
        lista_portales = tomar_objetos(lista['nivel2']['portales'], Portal)
        lista_enemigos = tomar_enemigo(lista['nivel2']['enemy'])
    elif level == 3:
        imagen_fondo = pygame.image.load(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources/background/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")
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
            pygame.mixer.music.stop()
            save_score(username, player_1.health)
            
            # --- INICIO DE CAMBIOS ---
            # Mostrar pantalla de ranking y esperar input
            pantalla_victoria = PantallaVictoria(screen)
            mostrar_ranking = True
            
            while mostrar_ranking:
                for event in pygame.event.get():
                    resultado = pantalla_victoria.manejar_eventos(event)
                    if resultado in ["menu", "salir"] or event.type == pygame.KEYDOWN:
                        mostrar_ranking = False
                
                pantalla_victoria.actualizar()
                pygame.display.update()
            # --- FIN DE CAMBIOS ---
            
            return  # Vuelve al menú principal (sin pasar por selector de niveles)

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
            bala.update_bullet(delta_ms, lista_characters, bulletmanager_1.balas_disparadas)  # Pasar listas necesarias
            bala.draw(screen)  # Dibujar la bala en pantalla
            # Verificar colisión con el jugador
            if player_1.rect_character_collition.colliderect(bala.bullet_rect) and not bala.player_bullet:
                player_1.health -= 10  # Reducir salud del jugador
                print(f"¡Jugador recibió daño! Salud restante: {player_1.health}")
                bulletmanager_1.balas_disparadas.remove(bala)  # Eliminar la bala tras la colisión

        pygame.display.flip()

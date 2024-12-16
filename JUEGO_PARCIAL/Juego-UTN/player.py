import pygame
from auxiliar import *
from bulletmanager import *
from bullet import *
from botiquin import *

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, healt, energia, bullets, live) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Run\Run-Sheet.png", 6, 1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Run\Run-Sheet_L.png", 6, 1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Idle\Idle-Sheet.png", 4, 1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Idle\Idle-Sheet_L.png", 4, 1)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Run\Run-Sheet.png", 6, 1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"resources\pixel\Heroes\Rogue\Run\Run-Sheet_L.png", 6, 1)

        # Sonidos
        self.botiquin_sound = pygame.mixer.Sound(r"resources\Sounds\SonidosVarios\plus.ogg")
        self.walk_sound = pygame.mixer.Sound(r"resources\Sounds\SonidosVarios\caminata.wav")
        self.jump_sound = pygame.mixer.Sound(r"resources\Sounds\SonidosVarios\grunt-106134.mp3")
        self.walk_sound.set_volume(0.5)
        self.is_walking_sound_playing = False  # Control del sonido de caminar

        # Atributos del jugador
        self.frame = 0
        self.lived = 1
        self.live = live
        self.energia = energia
        self.bullets = bullets
        self.health = healt
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_l
        self.direction = DIRECTION_L
        self.image = self.animation[self.frame]

        # Rectángulo principal del personaje
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        self.tiempo_transcurrido_move = 0  # Para gestionar el movimiento
        self.tiempo_transcurrido_animation = 0  # Para gestionar la animación
        self.tiempo_recuperacion_energia = 0  # Tiempo acumulado para regenerar energía
        self.intervalo_recuperacion = 1000  # Intervalo para regenerar energía (en ms)
        self.max_energia = 100  # Máximo de energía


        # Rectángulos de colisión iniciales
        self.rect_ground_collition = pygame.Rect(0, 0, 0, 0)
        self.rect_character_collition = pygame.Rect(0, 0, 0, 0)
        self.update_collitions()

        self.is_jump = False
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

    def update_collitions(self):
        # Ajustar rectángulos de colisión dependiendo del estado
        if self.animation in [self.walk_r, self.walk_l]:  # Caminando
            character_scale = 0.7
            ground_scale = 0.7
        else:  # Quieto o saltando
            character_scale = 0.8
            ground_scale = 0.8

        self.rect_character_collition = pygame.Rect(
            self.rect.x + self.rect.width * (1 - character_scale) / 2,
            self.rect.y + 25,
            self.rect.width * character_scale,
            self.rect.height * character_scale / 2
        )

        self.rect_ground_collition = pygame.Rect(
            self.rect.x + self.rect.width * (1 - ground_scale) / 2,
            self.rect.y + self.rect.height - GROUND_RECT_H,
            self.rect.width * ground_scale,
            GROUND_RECT_H
        )




    def set_sound_volume(self, enabled):
        """Ajusta el volumen de los sonidos del jugador según el estado de la música."""
        volume = 0.5 if enabled else 0  # 0.5 es el volumen normal, 0 es para silenciar
        self.walk_sound.set_volume(volume)
        self.jump_sound.set_volume(volume)
        self.botiquin_sound.set_volume(volume)



    def walk(self, direction):
        if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
            self.frame = 0
            self.direction = direction
            if direction == DIRECTION_R:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

        # Reproducir sonido de caminar si no está reproduciéndose
        if not self.is_walking_sound_playing:
            self.walk_sound.play(-1)
            self.is_walking_sound_playing = True

    def stay(self):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

        # Detener sonido de caminar
        if self.is_walking_sound_playing:
            self.walk_sound.stop()
            self.is_walking_sound_playing = False

    def jump(self, on_off=True):
        if self.energia <= 0:
            pass
        else:
            if on_off and not self.is_jump:
                self.y_start_jump = self.rect.y
                if self.direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_r
                    self.energia = max(0, self.energia - 20)
                    self.jump_sound.play()
                else:
                    self.move_x = -self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_l
                    self.energia = max(0, self.energia - 20)
                    self.jump_sound.play()
                self.frame = 0
                self.is_jump = True

            if not on_off:
                self.is_jump = False
                self.stay()

    def reducir_energia(self, cantidad):
        self.energia = max(0, self.energia - cantidad)

    def recuperar_energia(self, delta_ms):
        if self.energia < self.max_energia:
            self.tiempo_recuperacion_energia += delta_ms
            if self.tiempo_recuperacion_energia >= self.intervalo_recuperacion:
                self.energia += 5
                self.energia = min(self.energia, self.max_energia)
                self.tiempo_recuperacion_energia = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False
        if self.rect.y >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    retorno = True
                    break
        return retorno

    def check_trap_collision(self, lista_trampas):
        for trampa in lista_trampas:
            if self.rect_character_collition.colliderect(trampa.rect):
                self.health -= 10
                print(f"Jugador golpeado por trampa. Salud restante: {self.health}")
                lista_trampas.remove(trampa)

    def check_botiquin_collision(self, lista_botiquines):
        for botiquin in lista_botiquines:
            if self.rect_character_collition.colliderect(botiquin.rect):
                self.health += 30
                self.botiquin_sound.play()
                print(f"Jugador recogió un botiquín. Salud restante: {self.health}")
                lista_botiquines.remove(botiquin)

    def check_portal_collision(self, lista_portales):
        for portal in lista_portales:
            if self.rect_character_collition.colliderect(portal.rect):
                return True
        return False

    def is_shooted(self, lista_balas):
        current_time = pygame.time.get_ticks()
        for bala in lista_balas[:]:
            if isinstance(bala, Bullet):
                if self.rect_character_collition.colliderect(bala.bullet_rect) and not bala.player_bullet:
                    if current_time - self.last_hit_time >= self.damage_cooldown:
                        self.health -= 50
                        print(f"¡Jugador recibió daño! Salud restante: {self.health}")
                        self.last_hit_time = current_time
                        lista_balas.remove(bala)

    def state(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if hasattr(enemigo, 'health') and enemigo.health <= 0:
                enemigo.lived = 0
                lista_enemigos.pop(lista_enemigos.index(enemigo))

    def do_movement(self, delta_ms, lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0
            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            if not self.is_on_platform(lista_plataformas):
                self.add_y(self.gravity)
            elif self.is_jump:
                self.jump(False)

    def is_dead(self):
        return self.health <= 0

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def add_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_character_collition.x += delta_x

    def add_y(self, delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_character_collition.y += delta_y

    def update(self, delta_ms, lista_plataformas, lista_players, lista_balas, lista_trampas, lista_botiquines):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
        self.update_collitions()
        self.state(lista_players)
        self.check_trap_collision(lista_trampas)
        self.check_botiquin_collision(lista_botiquines)
        self.is_shooted(lista_balas)
        self.recuperar_energia(delta_ms)

    def draw(self, screen, lista_enemigos, scale_factor=1.0):
        self.image = self.animation[self.frame]
        scaled_image = pygame.transform.scale(
            self.image,
            (
                int(self.image.get_width() * scale_factor),
                int(self.image.get_height() * scale_factor)
            )
        )
        self.rect.width = scaled_image.get_width()
        self.rect.height = scaled_image.get_height()
        self.update_collitions()
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            pygame.draw.rect(screen, GREEN, self.rect_character_collition)
        screen.blit(scaled_image, self.rect)

    def events(self, keys):
        if keys[pygame.K_UP] and not self.is_jump:
            self.jump(True)
        if keys[pygame.K_LEFT]:
            self.walk(DIRECTION_L)
        elif keys[pygame.K_RIGHT]:
            self.walk(DIRECTION_R)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            self.stay()

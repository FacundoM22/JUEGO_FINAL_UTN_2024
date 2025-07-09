import pygame
from settings.auxiliar import *
from components.bullet import Bullet


class BulletManager():
    def __init__(self,cantidad_balas_player,cantidad_balas_enemigo):
        self.balas_player = [Bullet() for _ in range(cantidad_balas_player)]
        self.balas_enemy =  [Bullet() for _ in range(cantidad_balas_enemigo)]
        self.shoot_sound = pygame.mixer.Sound(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\Sounds\SonidosVarios\light-whoosh-241728.mp3")
        self.balas_disparadas = []
        self.cantidad_balas = cantidad_balas_player
        self.last_shot_time = 0  # Tiempo del último disparo


    def set_sound_volume(self, enabled):
        """Ajusta el volumen del sonido de disparo según el estado de la música."""
        volume = 0.5 if enabled else 0  # 0.5 es el volumen normal, 0 es para silenciar
        self.shoot_sound.set_volume(volume)

        

    def create_bullet(self,cantidad):
           return [Bullet() for _ in range(cantidad)] 

    def shoot(self, x_player, y_player, direction, controllable):
        current_time = pygame.time.get_ticks()  # Obtén el tiempo actual

        if controllable:  # Si el disparo es controlado por el jugador
            if self.balas_player and (current_time - self.last_shot_time >= 300):  # Cooldown de 300 ms
                self.last_shot_time = current_time
                bala_actual = self.balas_player.pop(0)
                bala_actual.player_bullet = True
                bala_actual.bullet_rect.x = x_player
                bala_actual.bullet_rect.y = y_player - 30
                bala_actual.shoot_direction = direction
                bala_actual.is_shooting = True
                self.balas_disparadas.append(bala_actual)
                self.shoot_sound.play()
                print("Bala disparada por el jugador")
            else:
                print("Esperando cooldown o sin balas disponibles")
        else:  # Si el disparo es de un enemigo
            if self.balas_enemy:
                bala_actual_enemigo = self.balas_enemy.pop(0)
                bala_actual_enemigo.bullet_rect.x = x_player
                bala_actual_enemigo.bullet_rect.y = y_player - 30
                bala_actual_enemigo.shoot_direction = direction
                bala_actual_enemigo.is_shooting = True
                self.balas_disparadas.append(bala_actual_enemigo)
                self.shoot_sound.play()
                print("Bala disparada por un enemigo")

           
        
    def reload(self):
             self.balas_player.clear()
             self.balas_player = self.create_bullet(self.cantidad_balas) 
             



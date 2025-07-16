import pygame
from settings.auxiliar import *
from settings.constants import DEBUG, RED  # Asegurá importar DEBUG y RED si no están

class Bullet:
    def __init__(self, x=0, y=0):
        # Usar get_ruta_absoluta para ruta correcta y consistente
        ruta_imagen = get_ruta_absoluta("../../resources/Bullet/fire.png")
        self.bullet = Auxiliar.getSurfaceFromSpriteSheet(ruta_imagen, 1, 1, True, 1, 2)
        self.frame = 0
        self.player_bullet = 0
        self.speed_bullet = 20
        self.move_x = 0
        self.is_shooting = False
        self.visible = False
        self.image_bullet = self.bullet[self.frame]
        self.bullet_rect = self.image_bullet.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
        self.shoot_direction = 0
        self.tiempo_transcurrido_bala = 0
        # Rectángulo de colisión centrado
        self.rect_bullet_collition = pygame.Rect(
            self.bullet_rect.x + 20,  # Desplazamiento para centrar el ancho
            self.bullet_rect.y + 20,  # Desplazamiento para centrar la altura
            self.bullet_rect.width - 40,  # Ancho reducido
            self.bullet_rect.height - 40  # Altura reducida
        )

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect_bullet_collition)  # Debug de colisión
        screen.blit(self.image_bullet, self.bullet_rect)

    def update_bullet(self, delta_ms, lista_characters, lista_balas):
        self.tiempo_transcurrido_bala += delta_ms

        for bala in lista_balas[:]:  # Usar copia para evitar errores al eliminar
            if bala.bullet_rect.x < -50 or bala.bullet_rect.x > 1550:
                bala.visible = False
                bala.is_shooting = False
                lista_balas.remove(bala)

        if self.tiempo_transcurrido_bala > 20:
            self.tiempo_transcurrido_bala = 0
            if self.is_shooting:
                if self.shoot_direction == DIRECTION_L:
                    self.bullet_rect.x -= self.speed_bullet
                elif self.shoot_direction == DIRECTION_R:
                    self.bullet_rect.x += self.speed_bullet

                # Actualiza el rectángulo centrado
                self.rect_bullet_collition = pygame.Rect(
                    self.bullet_rect.x + 20,
                    self.bullet_rect.y + 20,
                    self.bullet_rect.width - 40,
                    self.bullet_rect.height - 40
                )

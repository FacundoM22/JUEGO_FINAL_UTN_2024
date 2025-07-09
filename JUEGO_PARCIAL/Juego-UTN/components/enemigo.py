import pygame
from settings.auxiliar import *

class Enemigo:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,healt) -> None:
         self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Run\Run-Sheet.png", 6, 1)
         self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Run\Run-Sheet-Flipped.png", 6, 1)
         self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Idle\Idle-Sheet.png",4,1)
         self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Idle\Idle-Sheet-Flipped.png",4,1)
         self.jump_r =  Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Run\Run-Sheet.png", 6, 1)
         self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\pixel\Enemy\OrcCrew\OrcShaman\Run\Run-Sheet-Flipped.png", 6, 1)
         self.death_sound = pygame.mixer.Sound(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\Sounds\SonidosVarios\death.mp3")
         self.frame = 0
         self.lived = 1
         self.x_spot = x
         self.y_spot = y
         self.lives = 1
         self.health = healt
         self.move_x = 0
         self.move_y = 0
         self.speed_walk = speed_walk #Obtenido por parametro
         self.speed_run = speed_run
         self.gravity = gravity
         self.jump_power = jump_power
         self.animation = self.stay_l #Seteamos la animacion del personaje.
         self.direction = DIRECTION_L
         self.image = self.animation[self.frame] #Seleccionamos el frame de la lista animation.
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.is_jump = False
         self.tiempo_transcurrido_animation = 0
         self.tiempo_transcurrido_enemy_move = 0
         self.frame_rate_ms = frame_rate_ms
         self.tiempo_transcurrido_move = 0
         self.move_rate_ms = move_rate_ms
         self.y_start_jump = 0
         self.jump_height = jump_height
         self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
         self.rect_character_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + 25, self.rect.w / 4, self.rect.h / 2)


    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

    def jump(self,on_off = True):
     if(self.energia <= 0):
         pass
     else:
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                self.energia = self.energia - 20 # Energia
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                self.energia = self.energia - 20 # Energia
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()


    
    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)): #Comprobamos si existe una colision entre el rectangulo del personaje y el rectangulo de la plataforma
                    retorno = True
                    break   
        return retorno
    
    
    def is_shooted(self, lista_balas):
        for bala in lista_balas:
             if self.rect_character_collition.colliderect(bala.rect_bullet_collition) and bala.player_bullet == True:
                        self.health -= 50
                        print("Colisiono bala: {0}".format(bala.rect_bullet_collition))
                        print(self.health)
                        lista_balas.pop(lista_balas.index(bala))   


    def state(self,lista_enemigos):
        for enemigo in lista_enemigos:
                if enemigo.health <= 0:
                    enemigo.lived = 0
                    self.death_sound.play()
                    lista_enemigos.pop(lista_enemigos.index(enemigo))
                    




    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)


            if(self.is_on_platform(lista_plataformas) == False):
                 self.add_y(self.gravity)
            elif(self.is_jump): #Â SACAR
                self.jump(False)

 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_character_collition.x += delta_x

    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y
        self.rect_character_collition.y += delta_y


    def set_sound_volume(self, enabled):
        volume = 0.5 if enabled else 0  # 0.5 es el volumen normal, 0 es para silenciar
        self.death_sound.set_volume(volume)
        


    def update(self,delta_ms,lista_plataformas,lista_enemigos,lista_balas):
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)
        self.state(lista_enemigos)
        self.is_shooted(lista_balas)
        
    def draw(self, screen, lista_enemigos, scale_factor=1.0):
      
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)  # Rectángulo principal
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)  # Colisión suelo
            pygame.draw.rect(screen, GREEN, self.rect_character_collition)  # Colisión personaje

        # Actualizar la imagen actual del enemigo
        self.image = self.animation[self.frame]
        
        # Escalar la imagen si es necesario
        scaled_image = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor))
        )
        
        # Actualizar el rectángulo con el nuevo tamaño
        self.rect = scaled_image.get_rect(topleft=(self.rect.x, self.rect.y))
        
        # Actualizar los rectángulos de colisión
        self.rect_ground_collition = pygame.Rect(
            self.rect.x + self.rect.w / 3,
            self.rect.y + self.rect.h - GROUND_RECT_H * scale_factor,
            self.rect.w / 3,
            GROUND_RECT_H * scale_factor
        )
        self.rect_character_collition = pygame.Rect(
            self.rect.x + self.rect.w / 3,
            self.rect.y + 25 * scale_factor,
            self.rect.w / 4,
            self.rect.h / 2
        )
        
        # Dibujar la imagen escalada
        screen.blit(scaled_image, self.rect)




    def move_enemy(self,delta_ms,activate,bulletmanager): # Automatizacion del movimiento del enemigo
        if(self.rect.x == self.x_spot and self.rect.y == self.y_spot): 
           self.walk(DIRECTION_L)
           bulletmanager.shoot(self.rect.x,self.rect.y + 40, DIRECTION_L,False)
        elif ((self.x_spot - self.rect.x) > 100):
              self.walk(DIRECTION_R)
              bulletmanager.shoot(self.rect.x,self.rect.y + 40, DIRECTION_R,False)
        elif (self.rect.x == self.x_spot and self.rect.y == self.y_spot):
             self.walk(DIRECTION_R)
             bulletmanager.shoot(self.rect.x,self.rect.y + 40, DIRECTION_R,False)
        elif ((self.x_spot - self.rect.x) <-100):
            bulletmanager.shoot(self.rect.x,self.rect.y + 40, DIRECTION_L,False)
            self.walk(DIRECTION_L)
        

        

        
               
      
        
       



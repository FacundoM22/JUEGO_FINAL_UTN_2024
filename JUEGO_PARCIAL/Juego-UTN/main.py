import pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
from managers.db_manager import init_db
from core.menu import main_menu




init_db()  # Asumo que está definido en algún import global o en settings


main_menu()

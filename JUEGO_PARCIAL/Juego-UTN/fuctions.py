import pygame
import json
from enemigo import Enemigo
#from plataforma import Platform
#from trampa import Trampa
from portal import Portal




@staticmethod
def load_json_info(path):
    temp_list = []
    with open(path, 'r') as file:
        temp_list = json.load(file)
    return temp_list


def tomar_enemigo(lista) -> list:
    temp_list = []

    for objeto in lista:
        temp_list.append(Enemigo(
            x=objeto['x'],
            y=objeto['y'],
            speed_walk=objeto['speed_walk'],
            speed_run=objeto['speed_run'],
            gravity=objeto['gravity'],
            jump_power=objeto['jump_power'],
            frame_rate_ms=objeto['frame_rate_ms'],
            move_rate_ms=objeto['move_rate_ms'],
            jump_height=objeto['jump_height'],
            healt=objeto['healt'],
        ))
    return temp_list

def tomar_objetos(lista,tipo) -> list:
    temp_list = []

    for objeto in lista:
            temp_list.append(tipo(
            x=objeto['x'],
            y=objeto['y'],
            w=objeto['w'],
            h=objeto['h'],
            type=objeto['type']
            ))

    return temp_list





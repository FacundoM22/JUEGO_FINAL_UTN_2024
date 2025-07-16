# utils.py
import os

def get_ruta_absoluta(ruta_relativa_desde_este_archivo: str) -> str:
    base_path = os.path.dirname(__file__)
    return os.path.normpath(os.path.join(base_path, ruta_relativa_desde_este_archivo))


import sqlite3
from settings.auxiliar import *
from settings.ui_helpers import crear_botones
import sys
from settings.settings import get_fuente

DB_NAME = "ranking.db"

def init_db():
    """Inicializa la base de datos y crea la tabla si no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_score(username, score):
    """Guarda el puntaje del jugador en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ranking (username, score) VALUES (?, ?)", (username, score))
    conn.commit()
    conn.close()

def obtener_ranking(limit=10):
    """Obtiene los mejores puntajes, ordenados de mayor a menor."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username, score FROM ranking ORDER BY score DESC LIMIT ?", (limit,))
    ranking = cursor.fetchall()
    conn.close()
    return ranking



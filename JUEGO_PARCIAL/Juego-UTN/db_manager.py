
import sqlite3
from auxiliar import *
from ui_helpers import crear_botones
import sys

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

def get_top_scores(limit=10):
    """Obtiene los mejores puntajes, ordenados de mayor a menor."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username, score FROM ranking ORDER BY score DESC LIMIT ?", (limit,))
    ranking = cursor.fetchall()
    conn.close()
    return ranking


def show_ranking():
    music = pygame.mixer.Sound(r"resources\Sounds\win.ogg")
    # Fondo del ranking
    Background = pygame.image.load(r"resources/background/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640/backgroundMenu.png")
    Background = pygame.transform.scale(Background, (ANCHO_VENTANA, ALTO_VENTANA))

    # Crear botones para el ranking
    botones = crear_botones("ranking")

    # Obtener los datos del ranking desde la base de datos
    conn = sqlite3.connect("ranking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, score FROM ranking ORDER BY score DESC LIMIT 10")
    ranking = cursor.fetchall()
    conn.close()

    font = pygame.font.SysFont("Cambria", 30)

    while True:
        music.play()
        # Dibujar el fondo
        screen.blit(Background, (0, 0))

        # Título del ranking
        title = font.render("RANKING", True,  FUCHSIA)  # Texto en negro
        screen.blit(title, (ANCHO_VENTANA // 2 - title.get_width() // 2, 50))

        # Mostrar puntajes
        y_offset = 100
        for i, (user, score) in enumerate(ranking, start=1):
            text = font.render(f"{i}. {user}: {score}", True, FUCHSIA)  # Texto en negro
            screen.blit(text, (ANCHO_VENTANA // 2 - text.get_width() // 2, y_offset))
            y_offset += 40

        # Obtener la posición del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Dibujar los botones
        for button in botones.values():
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["menu_principal"].checkForInput(MENU_MOUSE_POS):  # Botón "Menú Principal"
                    music.stop()
                    return  # Regresa al menú principal
                if botones["salir"].checkForInput(MENU_MOUSE_POS):  # Botón "Salir"
                    pygame.quit()
                    sys.exit()

        # Actualizar la pantalla
        pygame.display.update()

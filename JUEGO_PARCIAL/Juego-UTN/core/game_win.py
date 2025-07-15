import pygame
from settings.ui_helpers import crear_botones
from settings.settings import ANCHO_VENTANA, ALTO_VENTANA
from settings.ui_helpers import IMAGEN_BOTON
from managers.db_manager import obtener_ranking
from settings.settings import get_fuente
from components.button import Button

class PantallaVictoria:
    def __init__(self, screen):
        self.screen = screen
        self.fuente_titulo = get_fuente(72)
        self.fuente_items = get_fuente(36)
        self.sonido_victoria = pygame.mixer.Sound(r"JUEGO_FINAL_UTN_2024\JUEGO_PARCIAL\resources\Sounds\win.ogg")
        self.botones = self._crear_botones()
        self.sonido_reproducido = False

    def _crear_botones(self):
        """Crea manualmente los botones para asegurar compatibilidad"""
        botones = {
            "menu": Button(
                image=IMAGEN_BOTON,
                pos=(ANCHO_VENTANA // 3, 500),
                text_input="MENU PRINCIPAL",
                font=self.fuente_items,
                base_color="#a9a9a9",
                hovering_color="#7faaff"
            ),
            "salir": Button(
                image=IMAGEN_BOTON,
                pos=(2 * ANCHO_VENTANA // 3, 500),
                text_input="SALIR",
                font=self.fuente_items,
                base_color="#a9a9a9",
                hovering_color="#ff7f7f"
            )
        }
        return botones

    def mostrar_ranking(self, top_n=5):
        """Muestra el ranking de puntuaciones"""
        if not self.sonido_reproducido:
            self.sonido_victoria.play()
            self.sonido_reproducido = True
            
        ranking = obtener_ranking()[:top_n]
        
        # Fondo semi-transparente
        fondo = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
        fondo.fill((0, 0, 0, 180))
        self.screen.blit(fondo, (0, 0))
        
        # Título
        titulo = self.fuente_titulo.render("🏆 RANKING 🏆", True, "#FFD700")
        self.screen.blit(titulo, (ANCHO_VENTANA//2 - titulo.get_width()//2, 50))
        
        # Items del ranking
        for i, (nombre, puntaje) in enumerate(ranking, start=1):
            y_pos = 150 + i * 50
            nombre = nombre if nombre else "ANÓNIMO"
            
            texto = f"{i}. {nombre:<12} {puntaje:>5} pts"
            item = self.fuente_items.render(texto, True, self._color_por_puesto(i))
            self.screen.blit(item, (ANCHO_VENTANA//2 - 200, y_pos))

    def _color_por_puesto(self, puesto):
        """Devuelve color según posición en el ranking"""
        colors = {
            1: "#FFD700",  # Oro
            2: "#C0C0C0",  # Plata
            3: "#CD7F32"   # Bronce
        }
        return colors.get(puesto, "#FFFFFF")

    def actualizar(self):
        """Actualiza todos los elementos de la pantalla"""
        self.mostrar_ranking()
        mouse_pos = pygame.mouse.get_pos()
        for boton in self.botones.values():
            boton.changeColor(mouse_pos)
            boton.update(self.screen)

    def manejar_eventos(self, event):
        """Maneja eventos de la pantalla"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for clave, boton in self.botones.items():
                if boton.checkForInput(mouse_pos):
                    return clave
        return None
# Juego:

**Videojuego hecho en Python (Pygame)** con el objetivo de familiarizarme con el lenguaje, inspirado en *GLITCH THE GAME*. Incluye distintos escenarios que el usuario puede seleccionar interactuando con menús. Cuenta con un sistema de ataque mediante balas, plataformas y gravedad. 

El objetivo del juego es completar los niveles con la mayor puntuación posible, lograda al eliminar enemigos y recolectar monedas. Al finalizar, el jugador debe ingresar al portal para concluir el nivel. Cada nivel tiene un **ranking TOP 10** con los mejores puntajes.

---

## Demo del Proyecto

Aquí puedes ver un video demostrativo del juego en acción:

[![Ver video](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/maxresdefault.jpg)](https://drive.google.com/file/d/1kFLGx_ke-waVkJksnOW7EMRiVJQZSXF8/view)

*(Haz clic en la imagen para ver el video)*

---

## Imágenes

### Menú Principal
![Menú Principal](https://private-user-images.githubusercontent.com/106789613/396240749-f27650c2-9697-4713-9c17-a7ae05a29b04.PNG?jwt=...)

### Juego
![Juego](https://private-user-images.githubusercontent.com/106789613/396240771-6d348571-f9f1-415c-8e1f-52c7668599dc.PNG?jwt=...)

### Game Over
![Game Over](https://private-user-images.githubusercontent.com/106789613/396240708-67d557bb-1f41-4806-93c7-14de22d5c772.PNG?jwt=...)

### Ranking
![Ranking](https://private-user-images.githubusercontent.com/106789613/396240807-d862eadf-6727-49a9-9ac7-c4994252ef6f.PNG?jwt=...)

---

## Preparación del entorno:

- Se requiere instalar Visual Studio Code.
- Se debe instalar Pygame.
- Ajustar `PATH_RECURSOS` y `PATH_JSON` con la dirección correspondiente.

---

## Características:

- Para guardar y acceder a la información del jugador se utiliza la biblioteca `sqlite3`.
- Todos los niveles son cargados mediante archivos JSON.
- Cuenta con un manejador de balas, lo que mejora la experiencia de juego, ya que las balas son independientes y no desaparecen tras eliminar enemigos o jugadores.

---

## Futuros cambios:

- Implementar un sistema de conteo de tiempo regresivo por nivel.
- Mejorar escenarios.
- Optimizar el diseño gráfico de formularios y la estructura general.
- Optimizar el rendimiento del juego.
- Implementar efectos de sonido.
- Añadir control de sonido (subir y bajar volumen).
- Mejorar cuadros de texto en calidad de diseño.
- Perfeccionar animaciones, como el impacto cuando un personaje recibe daño.

---

## Errores:

- Actualmente no es posible cargar música ni sonidos. No se carga la DLL "libmpg1230_.dll" (puede ser un problema local; si es así, omitir esta línea).

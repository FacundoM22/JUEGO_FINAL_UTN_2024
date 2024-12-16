# Juego:

Video juego hecho en Python (Pygame) con el objetivo de familiarizarme con el lenguaje, basado en GLITCH THE GAME. Esta conformado por distintos escenarios los cuales el usuario puede seleccionar interactuando con menus, cuenta con un sistema de ataque mediante balas, sistema de plataformas y gravedad. El objetivo del juego es pasar los distintos niveles con la mayor puntuacion posible eso se logra matando todos los enemigos presentes y recogiendo las monedas distribuidas en el escenario, luego hay que entrar al portal para concluir el nivel. Todos los niveles cuentan con un ranking en el cual se muestra el TOP 10 de los jugadores con mas puntuacion en cada uno.



## Imagenes:

  ### Menu principal:
  ![1](https://user-images.githubusercontent.com/106789613/207981969-fd872e60-6b44-4edc-b6af-4f8a0430e2a1.png)

  ### Juego:
  ![2](https://user-images.githubusercontent.com/106789613/207981981-d9a1f8a7-7884-4af0-b7b6-82967aeb5a1a.png)

  ### Game over:
  ![3](https://user-images.githubusercontent.com/106789613/207981990-3d4a861b-cf57-47ec-87fc-a649e91dfc5f.png)

  ### Ranking:
  ![4](https://user-images.githubusercontent.com/106789613/207981997-d3e47236-c534-4328-bd7a-64fb1496a633.png)

## Video:

https://user-images.githubusercontent.com/106789613/207989092-d470c960-1ffa-4154-8a4e-2acffe6b1c2b.mp4

# Preparación del entorno:

- Se requiere instalar Visual Studio Code
- Se debe instalar Pygame
- Ajustar PATH_RECURSOS y PATH_JSON con la dirección correspondiente.


# Caracteristicas:

- Para guardar y acceder a la informacion del jugador se utiliza la biblioteca SQLITE3.
- Todos los niveles son cargados mediante archivos JSON.
- Cuenta con un manejador de balas, lo que aumenta la experiencia de juego ya que al morirse un enemigo o jugador no desaparecen las balas disparadas, son independientes.


# Futuros cambios:

- Implementar sistema de conteo de tiempo regresivo por nivel.
- Mejorar escenarios.
- Optimización de  diseño gráfico de formularios, como también a nivel estructura.
- Optimización del juego.
- Implementar efectos de sonidos.
- Implementar control de sonido. (bajar y subir volumen)
- Mejora de cuadros de textos, en calidad de diseño.
- Mejorar animaciones, por ejemplo cuando un personaje recibe daño.


# Errores:

- No es posible cargar musica ni sonidosm no se carga la dll "libmpg1230_.dll" (puede ser a nivel local, si es así omitir esta linea)

# Juego:

Video juego hecho en Python (Pygame) con el objetivo de familiarizarme con el lenguaje, basado en GLITCH THE GAME. Esta conformado por distintos escenarios los cuales el usuario puede seleccionar interactuando con menus, cuenta con un sistema de ataque mediante balas, sistema de plataformas y gravedad. El objetivo del juego es pasar los distintos niveles con la mayor puntuacion posible eso se logra matando todos los enemigos presentes y recogiendo las monedas distribuidas en el escenario, luego hay que entrar al portal para concluir el nivel. Todos los niveles cuentan con un ranking en el cual se muestra el TOP 10 de los jugadores con mas puntuacion en cada uno.



## Imagenes:

  ### Menu principal:
  [![1](https://user-images.githubusercontent.com/106789613/207981969-fd872e60-6b44-4edc-b6af-4f8a0430e2a1.png)
](https://private-user-images.githubusercontent.com/106789613/396240749-f27650c2-9697-4713-9c17-a7ae05a29b04.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzQ5LWYyNzY1MGMyLTk2OTctNDcxMy05YzE3LWE3YWUwNWEyOWIwNC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MDM3ODEwNzVkY2U1ZWIxOGFhZGUzNTA4ODg2N2ZhZWE1Njk3ZjZlMzNjNDUwMWIzMzhkODU1NTRhYmMyMGM4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9bA-16v0qLTC9GqN4h2_6-R7P4Z_9vTthCbhoc1ROxk)
  ### Juego:
  ![2](https://user-images.githubusercontent.com/106789613/207981981-d9a1f8a7-7884-4af0-b7b6-82967aeb5a1a.png)

  ### Game over:
  ![3](https://user-images.githubusercontent.com/106789613/207981990-3d4a861b-cf57-47ec-87fc-a649e91dfc5f.png)

  ### Ranking:
  ![4](https://user-images.githubusercontent.com/106789613/207981997-d3e47236-c534-4328-bd7a-64fb1496a633.png)

### Demo del Proyecto
Este es un video demostrativo del proyecto:

<video src="https://private-user-images.githubusercontent.com/106789613/392188681-57bc6a07-992d-48ff-8866-159be4c2a86f.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNzU0NzcsIm5iZiI6MTczMzI3NTE3NywicGF0aCI6Ii8xMDY3ODk2MTMvMzkyMTg4NjgxLTU3YmM2YTA3LTk5MmQtNDhmZi04ODY2LTE1OWJlNGMyYTg2Zi5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIwNFQwMTE5MzdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNTcxY2JjZDNiZGNkZWRmMzRjODM1Y2UwYzM3OTBhN2QzZmQ2NWU0NWUwYWQyMmEzMGZjZGQxNjJlYWYyYzI4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.MPGy7caALR8t7iczLVyWnDlLFGD0e8lDiq8svt-R1RM" controls="controls" style="max-width: 100%;">
  Tu navegador no soporta la etiqueta de video.
</video>


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

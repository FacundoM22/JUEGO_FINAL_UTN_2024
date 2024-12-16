# Juego:

Video juego hecho en Python (Pygame) con el objetivo de familiarizarme con el lenguaje, basado en GLITCH THE GAME. Esta conformado por distintos escenarios los cuales el usuario puede seleccionar interactuando con menus, cuenta con un sistema de ataque mediante balas, sistema de plataformas y gravedad. El objetivo del juego es pasar los distintos niveles con la mayor puntuacion posible eso se logra matando todos los enemigos presentes y recogiendo las monedas distribuidas en el escenario, luego hay que entrar al portal para concluir el nivel. Todos los niveles cuentan con un ranking en el cual se muestra el TOP 10 de los jugadores con mas puntuacion en cada uno.



## Imagenes:

  ### Menu principal:
  ![1](https://private-user-images.githubusercontent.com/106789613/396240749-f27650c2-9697-4713-9c17-a7ae05a29b04.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzQ5LWYyNzY1MGMyLTk2OTctNDcxMy05YzE3LWE3YWUwNWEyOWIwNC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MDM3ODEwNzVkY2U1ZWIxOGFhZGUzNTA4ODg2N2ZhZWE1Njk3ZjZlMzNjNDUwMWIzMzhkODU1NTRhYmMyMGM4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9bA-16v0qLTC9GqN4h2_6-R7P4Z_9vTthCbhoc1ROxk)
  ### Juego:
  ![2](https://private-user-images.githubusercontent.com/106789613/396240771-6d348571-f9f1-415c-8e1f-52c7668599dc.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzcxLTZkMzQ4NTcxLWY5ZjEtNDE1Yy04ZTFmLTUyYzc2Njg1OTlkYy5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MzU4MGQ3YjBlYmM5Yjk2ODViMzYyNGYxMTgzNDVhY2Q0Yjk1MzMwOGM5OTViMGE1YjExNjUyNWM2OGQ2OGYwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.10o1_u363R0I1QQkShvxdy06Fn-MxIOapkIrEdZawV8)

  ### Game over:
  ![3](https://private-user-images.githubusercontent.com/106789613/396240708-67d557bb-1f41-4806-93c7-14de22d5c772.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzA4LTY3ZDU1N2JiLTFmNDEtNDgwNi05M2M3LTE0ZGUyMmQ1Yzc3Mi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZGIyNDA4ZGVkYjE4MjFhMGQxOTM4NzA3MTg0YmMzMDgxNjhlZGFiMWUwODRjOGRhZDcxMDkxMGEwMjFjZDI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.rK67NU5Y-NrM3S68myPA8a6uIIC0raLs7qq6IwPRv1Q)

  ### Ranking:
  ![4]([https://user-images.githubusercontent.com/106789613/207981997-d3e47236-c534-4328-bd7a-64fb1496a633.png](https://private-user-images.githubusercontent.com/106789613/396240807-d862eadf-6727-49a9-9ac7-c4994252ef6f.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwODA3LWQ4NjJlYWRmLTY3MjctNDlhOS05YWM3LWM0OTk0MjUyZWY2Zi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MWZhYWQyZDUwM2RhNTY5NmJmNzA2M2UxNTU0NTNiOGVkYjg2ZTFiYTU0MjUzMmQwNzRiMDI5ZTZiNDExMWU3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.waW0sO2_EMP62C7eulhe5YBMjET9eIG9yX31b6FKj_M))

### Demo del Proyecto
Este es un video demostrativo del proyecto:

<video src="https://drive.google.com/file/d/1kFLGx_ke-waVkJksnOW7EMRiVJQZSXF8/view?usp=sharing" controls="controls" style="max-width: 100%;">
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

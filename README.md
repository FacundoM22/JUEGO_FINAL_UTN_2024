# 🎮 Juego: 

**Videojuego hecho en Python (Pygame)** con el objetivo de familiarizarme con el lenguaje, combinando recursos de libre utilización. 🛠️ 

Incluye distintos escenarios que el usuario puede seleccionar interactuando con menús. 📜 Cuenta con un sistema de ataque mediante balas, plataformas (próximamente 🚧) y gravedad. 🌌

🎯 **Objetivo**: Completar los niveles con la mayor puntuación posible eliminando enemigos y recolectando monedas (a implementar 💰). Al finalizar, el jugador debe ingresar al portal para concluir el nivel. 🚪 Cada nivel incluye un **ranking TOP 10** para los mejores puntajes. 🏆

---

## 🎥 Demo del Proyecto

Video 👉 [Video en Google Drive](https://drive.google.com/file/d/1kFLGx_ke-waVkJksnOW7EMRiVJQZSXF8/view)

---

## 📸 Imágenes

### Menú Principal
![Menú Principal](https://private-user-images.githubusercontent.com/106789613/396240749-f27650c2-9697-4713-9c17-a7ae05a29b04.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzQ5LWYyNzY1MGMyLTk2OTctNDcxMy05YzE3LWE3YWUwNWEyOWIwNC5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MDM3ODEwNzVkY2U1ZWIxOGFhZGUzNTA4ODg2N2ZhZWE1Njk3ZjZlMzNjNDUwMWIzMzhkODU1NTRhYmMyMGM4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9bA-16v0qLTC9GqN4h2_6-R7P4Z_9vTthCbhoc1ROxk)

### Juego
![Juego](https://private-user-images.githubusercontent.com/106789613/396240771-6d348571-f9f1-415c-8e1f-52c7668599dc.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzcxLTZkMzQ4NTcxLWY5ZjEtNDE1Yy04ZTFmLTUyYzc2Njg1OTlkYy5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MzU4MGQ3YjBlYmM5Yjk2ODViMzYyNGYxMTgzNDVhY2Q0Yjk1MzMwOGM5OTViMGE1YjExNjUyNWM2OGQ2OGYwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.10o1_u363R0I1QQkShvxdy06Fn-MxIOapkIrEdZawV8)

### Game Over
![Game Over](https://private-user-images.githubusercontent.com/106789613/396240708-67d557bb-1f41-4806-93c7-14de22d5c772.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwNzA4LTY3ZDU1N2JiLTFmNDEtNDgwNi05M2M3LTE0ZGUyMmQ1Yzc3Mi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZGIyNDA4ZGVkYjE4MjFhMGQxOTM4NzA3MTg0YmMzMDgxNjhlZGFiMWUwODRjOGRhZDcxMDkxMGEwMjFjZDI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.rK67NU5Y-NrM3S68myPA8a6uIIC0raLs7qq6IwPRv1Q)

### Ranking
![Ranking](https://private-user-images.githubusercontent.com/106789613/396240807-d862eadf-6727-49a9-9ac7-c4994252ef6f.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzQzNzcyMjMsIm5iZiI6MTczNDM3NjkyMywicGF0aCI6Ii8xMDY3ODk2MTMvMzk2MjQwODA3LWQ4NjJlYWRmLTY3MjctNDlhOS05YWM3LWM0OTk0MjUyZWY2Zi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIxNlQxOTIyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MWZhYWQyZDUwM2RhNTY5NmJmNzA2M2UxNTU0NTNiOGVkYjg2ZTFiYTU0MjUzMmQwNzRiMDI5ZTZiNDExMWU3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.waW0sO2_EMP62C7eulhe5YBMjET9eIG9yX31b6FKj_M)

---

## 🛠️ Preparación del entorno

1. **Instalar Visual Studio Code**: Es necesario para editar y ejecutar el proyecto.
2. **Instalar Pygame**: La biblioteca principal para ejecutar el juego.
3. Ajustar las rutas `PATH_RECURSOS` y `PATH_JSON` según tu entorno. 📂

---

## ✨ Características

✅ Utiliza la biblioteca `sqlite3` para guardar y acceder a la información del jugador.  
✅ Los niveles se cargan mediante archivos JSON.  
✅ Manejador de balas independiente, mejorando la experiencia al mantener las balas activas incluso después de eliminar enemigos o jugadores. 💥

---

## 🚀 Futuros cambios

🔄 **Próximas mejoras**:  
- ⏱️ Implementar un sistema de tiempo regresivo por nivel.  
- 🎨 Mejorar los escenarios.  
- 🛠️ Optimizar el diseño gráfico de los formularios.  
- ⚡ Optimizar el rendimiento general del juego.  
- 🔊 Implementar efectos de sonido. *(Completado ✅)*  
- 🔉 Añadir control de volumen (subir y bajar sonido).  
- 📝 Mejorar cuadros de texto en diseño y legibilidad.  
- 🕺 Mejorar animaciones (por ejemplo, recibir daño).

---

## 🐞 Errores conocidos

❌ Actualmente no es posible cargar música ni sonidos debido a la DLL `libmpg1230_.dll`. *(Solucionado ✅)*  

---


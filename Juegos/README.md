# 🛸 SpaceMax Defender

¡Bienvenid@ a mi versión personalizada del clásico juego de naves espaciales!  
Este proyecto fue desarrollado en **Python** usando **Pygame**, y empaquetado con **Docker** para facilitar su ejecución en cualquier entorno.

---

## 🧠 Descripción

El objetivo del juego es controlar una nave espacial para destruir a los enemigos que descienden.  
Cada enemigo eliminado suma puntos. El juego termina cuando se acaban las vidas del jugador.

---

## 🎨 Personalización

Este juego fue modificado con mi estilo personal:  
🌸 Fondos rosados, gráficos personalizados, sonidos y estilo visual acorde a mis gustos.

---

## 📦 Estructura del proyecto

```
juego_naves/
├── assets/
│   ├── images/
│   └── sounds/
├── main.py
├── Dockerfile
└── README.md
```

---

## 🐳 Cómo ejecutar con Docker

### 1. Construir la imagen

```bash
docker build -t juego_naves .
```

### 2. Ejecutar el contenedor con acceso gráfico

```bash
xhost +local:docker
sudo docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix juego_naves
```

---

## 🖥️ Cómo ejecutar localmente (sin Docker)

> Requiere tener Python 3 y Pygame instalados

### 1. Activar entorno virtual (si aplica)

```bash
source venv/bin/activate
```

### 2. Ejecutar el juego

```bash
python main.py
```

---

## 🎮 Controles del juego

- ⬅️ ➡️ Mover la nave
- Barra espaciadora: Disparar

---

## ✨ Captura del juego

<p align="center">
  <img src="assets/images/preview.jpg" height="300" alt="Captura del juego" />
</p>

> 💡 Puedes tomar una captura y guardarla como `preview.jpg` en la carpeta `assets/images/`.

---

## 📍 Autor

- **Valentina** – Estudiante de Ingeniería Electrónica  
- Me encantan los videojuegos, los animales y el color rosado 💖

---

¡Gracias por visitar mi proyecto! 🚀


# 🛡️ Tank Battle – Juego Clásico de Tanques

Bienvenida al proyecto **Tank Battle**, un videojuego clásico tipo arcade creado en **Python con Pygame**, donde controlas un tanque personalizado y debes enfrentarte a enemigos que atacan por oleadas. ¡Incluye imágenes y diseño únicos con tu estilo! 🌸

---

## 🧩 Descripción

- 🚀 Juego estilo arcade: controlas un tanque y disparas a enemigos.
- 🎨 Personalización completa con imágenes y estilo rosado.
- 🔫 Enemigos con IA básica que también disparan.
- ❤️ Sistema de salud, puntuación y dificultad progresiva.

---

## 📷 Captura del juego

<p align="center">
  <img src="assets/images/captura.png" alt="Captura del juego" width="600"/>
</p>

---

## 🔧 Tecnologías utilizadas

<p align="center">
  <img src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/pygame-%2300B140.svg?style=for-the-badge&logo=pygame&logoColor=white" />
  <img src="https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white" />
</p>

---

## 🗂️ Estructura del proyecto



# 🎮 Tetris Retro Gamer

![Tetris](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3p0cnE0eGJ2Z2pkZWFqZGE4NnAzcXdkN2V6b2hnc29ybDVuaGRzZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l1J9urxvEOY3zJHTG/giphy.gif)

---

## 🧩️ Descripción

**Tetris Retro Gamer** es una versión personalizada del clásico Tetris, desarrollado en Python con la librería `pygame`, y rediseñado con un estilo **gamer retro** usando colores neón y un fondo oscuro. El juego aumenta la velocidad de caída de las fichas a medida que subes de nivel y muestra un mensaje "Game Over" al perder, esperando una tecla antes de cerrar.

---

## 📦 Estructura del proyecto

```
juego_tetris_retro/
├── main.py
├── assets/
│   ├── images/ (opcional)
│   └── sounds/ (opcional)
├── Dockerfile
└── README.md
```

---

## 🔹 Controles

| Tecla        | Acción                     |
|--------------|----------------------------|
| ⬅️ / ➡️       | Mover pieza lateralmente   |
| ⬇️           | Acelerar caída             |
| ⬆️           | Rotar pieza                |
| ❌           | Cierra la ventana          |

---

## 🚀 Características

- ✔️ Estética retro con colores neón
- ✔️ Aumento de velocidad progresiva por niveles
- ✔️ Sistema de puntaje y niveles en pantalla
- ✔️ Mensaje de **Game Over** y espera al finalizar

---

## 🐍 Requisitos

- Python 3.8 o superior
- pygame

Instalar pygame:

```bash
pip install pygame
```

---

## ▶️ Ejecución

```bash
python3 main.py
```

---

## 🐳 Docker

Construcción:

```bash
docker build -t vale0109/juego_tetris_retro .
```

Ejecución:

```bash
xhost +local:docker
sudo docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix vale0109/juego_tetris_retro
```

---

## 🧠 Autora

Desarrollado por **Valentina** 💗  
Estudiante de Ingeniería Electrónica | Gamer | Amante de los animales

---

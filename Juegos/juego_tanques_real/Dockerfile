FROM python:3.8-slim

# Instalar librerías del sistema necesarias para Pygame
RUN apt-get update && apt-get install -y \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libfreetype6-dev libavformat-dev libswscale-dev \
    libsm6 libxext6 libxrender1 libx11-6 x11-xserver-utils \
    && apt-get clean

# Crear carpeta de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar pygame con pip
RUN pip install pygame

# Ejecutar el juego
CMD ["python3", "main.py"]

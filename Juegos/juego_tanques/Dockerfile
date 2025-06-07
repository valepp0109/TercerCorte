FROM python:3.10-slim

# Instala dependencias necesarias
RUN apt-get update && \
    apt-get install -y python3-tk python3-dev libgl1-mesa-glx && \
    pip install pygame

# Crea directorio de trabajo y copia archivos
WORKDIR /app
COPY . /app

# Ejecuta el juego
CMD ["python", "main.py"]

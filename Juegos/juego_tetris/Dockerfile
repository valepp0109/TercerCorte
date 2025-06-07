FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    python3-pygame \
    x11-xserver-utils \
    libx11-6 \
    libxext6 \
    libsm6 \
    libxrender1 && \
    apt-get clean

WORKDIR /app

COPY . .

CMD ["python3", "main.py"]

Tarea 9
readme
# 🎭 Proyecto: Reconocimiento de Emociones con Pepper

Este repositorio documenta paso a paso el desarrollo de un sistema de reconocimiento de emociones, como parte de una tarea académica en robótica social e inteligencia artificial. El proyecto fue desarrollado usando el robot **Pepper**, la herramienta **Roboflow** para la creación del dataset, y herramientas de documentación como GitHub y Overleaf.

---

## 📌 Objetivo general

Diseñar un pipeline que permita capturar una imagen facial desde Pepper, clasificarla en una de 4 emociones (feliz, triste, enojado, sorprendido), y documentar todo el proceso técnico y conceptual detrás de la solución.

---

## 🧩 Paso 1: Creación del Dataset de Emociones en Roboflow

El primer gran paso fue la elaboración de un dataset propio utilizando la plataforma [Roboflow](https://roboflow.com), el cual contenía imágenes clasificadas en 4 emociones. El proceso completo se detalló cuidadosamente para asegurar calidad y balance.

### 1.1 Creación del proyecto

- Se ingresó a Roboflow y se creó un nuevo proyecto con el nombre `Emotion Recognition`.
- Se seleccionó el tipo de proyecto como:  
  ➤ **Classification**  
  ➤ **Single-label** (porque cada imagen representa una única emoción).
- Se dejó el tipo de licencia como `CC BY 4.0`.

### 1.2 Estructura del dataset

- Se definieron 4 clases de emociones:
  - `happy` (feliz)
  - `sad` (triste)
  - `angry` (enojado)
  - `surprised` (sorprendido)
- Se subieron 10 imágenes por clase, completando un total de **40 imágenes**.

### 1.3 Etiquetado y verificación

- Cada imagen fue etiquetada manualmente en la sección de **"Annotate"** de Roboflow.
- Se verificó que todas las imágenes tuvieran su etiqueta correspondiente.
- Se revisó la sección **"Classes & Tags"** para confirmar que había exactamente 10 imágenes por clase.

### 1.4 Generación del dataset

- Se accedió a la sección **"Versions"** y se creó una nueva versión del dataset (`v1`).
- **No se aplicó augmentación** (rotación, brillo, etc.) para mantener las imágenes originales.
- Se seleccionó el tamaño de imagen sugerido (224x224 píxeles).
- Al finalizar, se generó la versión lista para exportación y/o entrenamiento.

---

## 📸 Paso 2: Captura de imagen desde Pepper

Se corrigió el código base proporcionado por la guía para que pudiera capturar una imagen desde la cámara de Pepper y almacenarla en la carpeta `D3/Cámara`.

### Código corregido:

```python
photo_service = session.service("ALPhotoCapture")
photo_service.setResolution(2)
photo_service.setPictureFormat("jpg")

# Guardar la imagen como "image.jpg" en la carpeta específica
photo_service.takePicture("/home/nao/recordings/cameras/", "image")

# Mostrar la imagen capturada en la pantalla del robot
tablet_service = session.service("ALTabletService")
tablet_service.showImage("http://198.18.0.1/apps/camera/image.jpg")

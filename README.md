# Rally MTB Tandil 2025

Este proyecto es una aplicación web desarrollada con **Flask** para la inscripción y difusión del evento **Rally MTB Tandil 2025**.  
La página muestra la información del evento, auspiciantes, kit de carrera y un formulario de inscripción que envía confirmaciones por correo electrónico.

---
## 📝 Funcionalidades principales

- **Página principal (`index.html`)**
  - Información general del evento (nombre, fecha, lugar, descripción).
  - Modalidades de carrera (30 km y 80 km).
  - Mapa del recorrido con puntos de hidratación.
  - Kit del corredor.
  - Sección de auspiciantes.
  - Descarga de reglamento y deslinde en PDF.

- **Formulario de inscripción (`registration.html`)**
  - Campos solicitados:
    - Nombre y Apellido
    - Email
    - Teléfono / Celular
    - Ciudad / Provincia
    - Teléfono de emergencia
    - Modalidad de carrera
  - Al enviar:
    - El competidor recibe un correo confirmando su inscripción.
    - La organización recibe un correo con los datos completos del competidor.
  - Mensajes de confirmación con `flash()`.

---

## ⚙️ Tecnologías utilizadas

- **Python 3**
- **Flask**
- **Flask-Mail**
- **HTML5 / CSS3**
- **Google Maps Embed** para el recorrido

---

## 📧 Envío de correos

La app usa **Flask-Mail** para enviar dos tipos de correos:

1. **Al participante**: confirmación de su inscripción y categoría elegida.  
2. **A la organización**: notificación con todos los datos cargados en el formulario.

La configuración de correo se gestiona mediante variables de entorno en un archivo `.env`:
---

## 🔑 Seguridad

- Se utiliza `app.secret_key` para manejar sesiones y mostrar mensajes flash.
- Las credenciales de correo no se guardan en el código, sino en el archivo `.env`.

---

## 🚀 Ejecución

1. Clonar el repositorio.
2. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
3. Instalar dependencias:
   ```
   pip install flask flask-mail python-dotenv
4. Ejecutar la aplicación con Flask:
   ```
   flask run --port=5001

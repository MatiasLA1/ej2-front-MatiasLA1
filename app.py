import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv


# Cargar variables de entorno del archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"  # necesario para flash()/

info_evento = {
    1: { "nombre": "Rally MTB 2025",
    "organizador": "Club Social y Deportivo Unidos por el Deporte",
    "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km. Viví la experiencia del mountain bike en uno de los paisajes más desafiantes de la Argentina. Una jornada única de deporte, naturaleza y adrenalina.",
    "fecha": "16 de noviembre de 2025",
    "horario": "8am",
    "lugar": "Tandil, Buenos Aires",
    "tipo_carrera": "MTB rural",
    "modalidad_costo": {
    1: {"nombre": "Corta" ,"valor": "100"},
    2: {"nombre": "Larga" ,"valor": "200"}},
    "Auspiciantes": ["Powerade","Specialized"]
    }
}


# # Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html',
                           nombre=info_evento[1]["nombre"],
                           organizador=info_evento[1]["organizador"],
                           nombre_evento=info_evento[1]["nombre"],
                           descripcion_evento=info_evento[1]["descripcion"],
                           tipo_carrera=info_evento[1]["tipo_carrera"],
                           fecha=info_evento[1]["fecha"],
                           lugar=info_evento[1]["lugar"],
                           )

@app.route('/base')
def base():
    return render_template('base.html',organizador=info_evento[1]["organizador"],nombre_evento=info_evento[1]["nombre"])

@app.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
            nombre = request.form.get("fname")
            apellido = request.form.get("lname")
            email_user = request.form.get("email")
            modalidad = request.form.get("modalidad_carrera")

            try:
                # Mail al participante
                msg_user = Message(
                    subject="Confirmación de inscripción - Rally MTB Tandil 2025",
                    recipients=[email_user]
                )
                msg_user.body = f"""
                Hola {nombre} {apellido}, gracias por inscribirte al Rally MTB Tandil 2025.
                Tu inscripción en la categoría {modalidad} ha sido recibida con éxito.
                Nos pondremos en contacto contigo con más detalles próximamente.
                ¡Nos vemos en la carrera!
                Equipo de Organización
                """
                mail.send(msg_user)

                # Mail al organizador
                msg_org = Message(
                    subject=f"Nueva inscripción: {nombre} {apellido}",
                    recipients=["mlaguilar@fi.uba.ar"]  #acá el mail de la organización
                )
                msg_org.body = f"""
                Nueva inscripción recibida:

                Nombre: {nombre} {apellido}
                Email: {email_user}
                Categoría: {modalidad}
                """
                mail.send(msg_org)

                flash("Inscripción enviada y confirmación enviada por correo.", "success")
            except Exception as e:
                flash(f"Ocurrió un error al enviar los correos: {e}", "danger")
            return redirect(url_for("registration"))
    
    return render_template('registration.html',
    organizador=info_evento[1]["organizador"],nombre_evento=info_evento[1]["nombre"])

if __name__ == '__main__':
    app.run("localhost",port=5001,debug=True)
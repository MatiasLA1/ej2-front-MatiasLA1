from flask import Flask, render_template, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

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

@app.route('/registration')
def registration():
    return render_template('registration.html',
    organizador=info_evento[1]["organizador"],nombre_evento=info_evento[1]["nombre"])

if __name__ == '__main__':
    app.run("localhost",port=5001,debug=True)
from flask import Flask, render_template, url_for

app = Flask(__name__)

info_evento = {
    1: { "nombre": "Rally MTB 2025",
    "organizador": "Club Social y Deportivo Unidos por el Deporte",
    "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
    "fecha": "24 de Octubre de 2025",
    "horario": "8am",
    "lugar": "Tandil, Buenos Aires",
    "tipo_carrera": "MTB rural",
    "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"},
    2: {"nombre": "Larga" ,"valor": "200"}},
    "Auspiciantes": ["ausp1","auspN"]
    }
}

@app.route('/')
def index():
    return render_template('index.html',organizador=info_evento[1]["organizador"],nombre_evento=info_evento[1]["nombre"])

@app.route('/base')
def base():
    return render_template('base.html',organizador=info_evento[1]["organizador"],nombre_evento=info_evento[1]["nombre"])

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run("localhost",port=5001,debug=True)
#!/bin/bash

# Nombre del proyecto
PROYECTO="TP2-IDS"

# Crear carpeta del proyecto
mkdir $PROYECTO
cd $PROYECTO

python3 -m venv .venv
source .venv/bin/activate

mkdir static templates

cd static
mkdir css images
cd ../

# Crear archivo app.py vacío
touch app.py
pip3 install flask

echo "Proyecto Flask '$PROYECTO' creado."
echo "-> Para activar el entorno virtual de nuevo usa:"
echo "   source .venv/bin/activate"

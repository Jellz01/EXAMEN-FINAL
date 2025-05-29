from flask import Flask
from flask_socketio import SocketIO, send
import threading
import time
import datetime
import os

USUARIOS = {
    "joseph": "1234",
    "admin": "adminpass"
}

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def mensaje_periodico():
    while True:
        socketio.emit('message', 'hola joseph')
        time.sleep(10)

@socketio.on('connect')
def handle_connect():
    send('hola joseph')
@socketio.on('message')
def handle_message(msg):
    # Menú numérico y comandos
    if msg == "1":
        respuesta = "Has seleccionado 'Eco'. Escribe: ECO tu_mensaje"
    elif msg == "2":
        respuesta = "Has seleccionado 'Sumar'. Escribe una suma, por ejemplo: 4+5"
    elif msg == "3":
        respuesta = datetime.datetime.now().strftime("Hora del servidor: %Y-%m-%d %H:%M:%S")
    elif msg == "4":
        respuesta = "Has seleccionado 'Leer archivo'. Escribe: FILE nombre_archivo.txt"
    elif msg == "5":
        respuesta = "Has seleccionado 'Login'. Escribe: usuario:clave"
    elif msg == "6":
        respuesta = "Has seleccionado 'Crear archivo'. Escribe: CREATE nombre_archivo.txt contenido"
    elif msg == "0":
        respuesta = "Gracias por usar el sistema. Hasta luego."
    elif msg == "GET TIME":
        respuesta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif msg.startswith("ECO "):
        respuesta = msg[4:]
    elif "+" in msg:
        try:
            respuesta = str(eval(msg))
        except:
            respuesta = "Operación inválida."
    elif msg.startswith("FILE "):
        filename = msg[5:].strip()
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                respuesta = f.read(500)
        else:
            respuesta = "Archivo no encontrado."
    elif msg.startswith("CREATE "):
        try:
            partes = msg[7:].strip().split(" ", 1)
            if len(partes) != 2:
                respuesta = "Formato incorrecto. Usa: CREATE nombre_archivo.txt contenido"
            else:
                nombre_archivo, contenido = partes
                with open(nombre_archivo, "w") as f:
                    f.write(contenido)
                respuesta = f"Archivo '{nombre_archivo}' creado correctamente."
        except Exception as e:
            respuesta = f"Error al crear archivo: {e}"
    elif ":" in msg:
        user, pwd = msg.split(":", 1)
        if USUARIOS.get(user) == pwd:
            respuesta = "LOGIN OK"
        else:
            respuesta = "LOGIN FAILED"
    else:
        respuesta = "Comando desconocido"
    send(respuesta)

if __name__ == '__main__':
    hilo = threading.Thread(target=mensaje_periodico)
    hilo.daemon = True
    hilo.start()
    socketio.run(app, host='0.0.0.0', port=8000)
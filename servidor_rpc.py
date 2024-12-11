from flask import Flask, jsonify
from xmlrpc.server import SimpleXMLRPCServer
import threading

# Iniciar la aplicación Flask
app = Flask(__name__)

# Función para servir la página HTML
@app.route('/')
def serve_html():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HELLOO WORLD!! RPC</title>
    </head>
    <body>
        <h1>¡Hello, World of RPC!</h1>
    </body>
    </html>
    """
    return html

# Función RPC que retorna el HTML
def obtener_pagina_html():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HELLOO WORLD!! RPC</title>
    </head>
    <body>
        <h1>¡Hello, World of RPC!</h1>
    </body>
    </html>
    """
    return html

# Iniciar el servidor XML-RPC en un hilo separado
def start_rpc_server():
    server = SimpleXMLRPCServer(('0.0.0.0', 8001))
    print("Servidor RPC en el puerto 8001...")
    server.register_function(obtener_pagina_html, "obtener_pagina_html")
    server.serve_forever()

# Crear y ejecutar el servidor RPC en un hilo separado
rpc_thread = threading.Thread(target=start_rpc_server)
rpc_thread.daemon = True
rpc_thread.start()

# Ejecutar el servidor Flask para servir la página HTML en el puerto 8000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

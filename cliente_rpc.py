import xmlrpc.client
import webbrowser

# Conectar al servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Llamar a la función remota para obtener la página HTML
html = proxy.obtener_pagina_html()

# Guardar el HTML en un archivo local
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

# Abrir la página en el navegador
webbrowser.open("index.html")

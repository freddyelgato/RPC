from xmlrpc.server import SimpleXMLRPCServer


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

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC Port 8000...")


server.register_function(obtener_pagina_html, "obtener_pagina_html")


server.serve_forever()

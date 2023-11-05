import http.server
import socketserver
from pyngrok import ngrok

# Configura el puerto en el que quieres que ngrok exponga tu servidor local >
port = 80

# Crea un servidor HTTP simple que siempre responde con un estado 200 OK
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

# Inicia el servidor HTTP en el puerto especificado
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Servidor HTTP en http://localhost:{port}")

    # Inicia ngrok y abre un túnel para el puerto especificado (HTTP)
    public_url = ngrok.connect(port, "http")

    print("Túnel ngrok disponible en:", public_url)

    try:

        # Mantén el servidor en ejecución
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# Para detener ngrok y cerrar el túnel cuando hayas terminado
ngrok.disconnect(public_url)


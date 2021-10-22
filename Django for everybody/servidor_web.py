"""
El servidor se despierta para esperar conexiones entrantes.
cuando comienzas a hablar con un servidor web, ese servidor ya está en esa computadora.
Registra su interés en las solicitudes entrantes.

El programa hará eso, se quedrá esperando en un bucle infinito para las solicitudes entrantes.

- Primero se crea un socket, haciendo el telefono, depende de nosotros deciir si vamos a llamar o recibir.
- si se ejecuta 2 veces, el segundo programa explotará porque no puede recibir llamadas en este servidor en el puerto 9000
- accept es un bloqueo, solo ejecuta cuando recibe llamada.
- El protocolo http recuelve el problema de decir "hola"
- El servidor sabe que el cliente debe hablar primero 
"""
from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) #crea el telefono
    try:
        serversocket.bind(('localhost',9000)) #conexión al puerto para recibir llamadas
        serversocket.listen(5) #rsi recibe una llamada, quedan 4 a las cuales aferrar en cola, si no se coloca, automaticamente negará la llamada.
        while(1):
            (clientsocket, address) = serversocket.accept()#registra numero y extensión; está listo para recoger el telefono. Bloquea, se detiene y se queda esperando indefinidamente

            rd = clientsocket.recv(5000).decode('utf-8') #consigue 5000 caracteres, tiene parametro GET, decodificado para Unicode en py.
            pieces = rd.split('\n')
            if (len(pieces)>0) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())#codifico antes de enviarlo
            clientsocket.shutdown(SHUT_WR) #apagado

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    
    serversocket.close()

print('Access http://localhost:9000')
createServer()

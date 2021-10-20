import socket

"""
Los sockets funcionan como archivos a los que podemos
enviar y recibir datos. 
Cuando estas usando un archivo en python primero debes abrirlo.
La apertura de un socket es un proceso de 2 pasos:
    1. crea el socket y este vive en la computadora como un punto 
    final que aún no ha terminado. Es el punto final al que vas a
    enviar y recibir datos dentro del ordenador. 

como navegador debemos primero hablar o escuchar, asi que enviamos la solicitud. 
Telnet era como un socket, podía conectarse a cualquier host, puerto, escribir cosas y ver
si está roto o no. 
El protocolo dice: una vez que el servidor ha recibido la primera linea, cualquier encabezado, y luego una linea
en blanco, entonces es devolverlo. 
Entonces la siguiente parte es donde vamos a tener un pequeño bucle. 
El protocolo dice que debemos recibir datos hasta que el socket esté cerrado. 
En la parte inferior de telnet se envian un monton de lineas, como 4

"""

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #es como hacer un telefono 
mysock.connect(('data.pr4e.org', 80)) #es como marcar el telefono, para el caso a un nombre de dominio y un puerto en ese dominio
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #Get seguido de un espacio, seguido de la URL 
#encode envía por internet en UTF-8 desde la consola que está originalmente en unicode. 
mysock.send(cmd) #cmd tiene una cadena UTF-8 y lo enviamos

while True: #estamos recuperando datos
    data = mysock.recv(512) #recibir, esto espera hasta que haya recibido 512 caracteres
    if len(data)<1:         #si no obtenemos ningun dato, se indica que la conexión de red, el socket, ha sido colgada, cerrada, por el servidor remoto. 
        break #es por eso que se rompe si la longitud de los datos es menor a 1
    print(data.decode(), end='')#sino vamos a imprimir los datos

mysock.close()
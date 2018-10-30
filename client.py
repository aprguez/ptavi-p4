#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

"""
Constantes. Dirección IP del servidor y contenido a enviar
"""

#Direccion IP
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
PETICIONES = sys.argv[3]
DIRECCIONSIP = sys.argv[4]
EXPIRES = sys.argv[5]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))
 
print("Enviando: " + PETICIONES + " sip: " + DIRECCIONSIP + '\r\n' + "Expires: " + EXPIRES)
my_socket.send(PETICIONES + " sip: " + DIRECCIONSIP  + " SIP/1.0 " + '\r\n' + "Expires: " + EXPIRES + '\r\n\r\n')
data = my_socket.recv(1024) #tamaño del buffer
        
print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket. . .")
    
#cerrando la conexion
my_socket.close()
print("Closed.")
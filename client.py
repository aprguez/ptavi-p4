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
SERVER = 'localhost'
PORT = int(sys.argv[2])
IP = sys.argv[1]

#Contenido a enviar    
LINE = sys.argv[3]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))
 
print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)
        
print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket. . .")
    
#cerrando la conexion
my_socket.close()
print("Closed.")
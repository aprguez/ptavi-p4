#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        Direccion y puerto del cliente
        """
        self.diccionario = {}
        while 1:
            line = self.rfile.read()
            lista = line.split(" ")
            if lista[0] == "REGISTER":
                self.diccionario[lista[1]] = self.client_address[0]
                print("El cliente nos manda " + lista[1] + " 200 OK\r\n\r\n")
                self.wfile.write(lista[1] + "OK\r\n\r\n")
            
            if not line:
                break

if __name__ == "__main__":
    # Servidor de eco para escucha
    serv = socketserver.UDPServer(("", int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
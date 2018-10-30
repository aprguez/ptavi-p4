#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        IP = self.client_address[0]
        PORT = self.client_address[1]
        print("IP: ", IP, "PORT: ", PORT)
        while 1:
            line = self.rfile.read()
            print(line)
            print("El cliente nos manda " + line.decode('utf-8'))
            
            if not line:
                break

if __name__ == "__main__":
    # Listens at localhost ('') port 6001 
    # and calls the EchoHandler class to manage the request
    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), EchoHandler) 
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
from time import gmtime, strftime, time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    Dicc = {}

    def register2json(self):
        """
        Creamos fichero json
        """
        print("register.Json")
        nombreJson = "registered.json"
        with open(nombreJson, 'w') as fichero_json:
                json.dump(self.dicc, fichero_json)

    def json2registered(self):
        try:
            with open("register.json", 'r') as existe:
                self.Dicc = json.load(existe)
        except:
            pass

    def deleteDicc(self):
        lista = []
        formato = '%Y-%m-%d %H:%M:%S'
        for clave in self.Dicc:
            valor = self.Dicc[clave][1]
            print(valor)
            if time.strptime(valor, formato) <= time.gmtime(time.time()):
                lista.append(clave)
        for usuario in lista:
            del self.Dicc[usuario]

    def handle(self):

        IP = self.client_address[0]
        PORT =  self.client_address[1]
        print("IP: ", IP, "PORT: ", PORT)
        if len(self.Dicc) == 0:
            self.json2registered()
            self.wfile.write(b"SIP/2.0 200 OK" + b"\r\n" + b"\r\n")
        while 1:

            line = self.rfile.read()
            metodo = line.decode('utf-8').split(" ")[0]
            if metodo == 'REGISTER':
                user = line.decode('utf-8').split(" ")[1]
                expires = line.decode('utf-8').split(" ")[2].split("\r\n")[1]
                valor = int(expires) + int(time())
                formato = "%a, %d %b %Y %H:%M:%S +0000"
                tiempo = strftime(formato, gmtime(valor))
                address = str(IP) + ":" + str(PORT)
                self.dicc[user] = ["address: " + address, "expires: " + tiempo]
                if int(expires) == 0:
                    print("Eliminando: " + user + ":" + str(self.dicc[user]))
                    del self.dicc[user]
                self.eliminarDicc()
                self.register2json()
                print (self.dicc)
            if not line:
                break

if __name__ == "__main__":

    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.allow_reuse_address = True
    serv.serve_forever()
    serv.close()

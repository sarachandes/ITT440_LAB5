import socket
import os
import sys

def Main():
    host = '192.168.56.102'
    port = 8080

    s = socket.socket()
    s.bind((host,port))
    print("server Mula")
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Bersambung dari: " + str(addr))
        filename = ''
        while True:
            data = c.recv(1024).decode('utf-8')
            if not data:
                break
            filename += data
        print("Dari user: " + filename)
        myfile = open(filename, "rb")
        c.send(myfile.read())
        c.close()

if __name__ == '__main__':
    Main()

import socket
import sys
import json
import os.path

def Main():
    host = '192.168.56.102'
    port = 8080

    s = socket.socket()
    s.connect((host, port))

    Filename = input("Tulis File ")
    s.send(Filename.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(1024).decode('utf-8')
    print(data)
    s.close()

if __name__ == '__main__':
    Main()

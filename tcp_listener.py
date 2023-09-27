#! usr/bin/python3

import socket

ip = 'enter ip to scan'
port = 'enter port to scan'
buffer = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.silent(1)

conn, addr = s.accept()

while True:
    data=conn.recv(buffer)
    if not data:
        break
    print("data recieved:  ", data)
    conn.send(data) #echo

conn.close()
import socket
import numpy as np 


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def send_Image(fileName = str):
    file = open(fileName,"rb")
    while True:
        buffer = file.read(1024)
        if buffer == b'':
            break
        buffer_len = len(buffer)
        send_length = str(buffer_len).encode(FORMAT)
        
        send_length += b' ' * (HEADER - len(send_length))
        
        client.send(send_length)
        print(send_length)
        client.send(buffer)
        
        print(client.recv(16).decode(FORMAT))
        
        
send_Image('deneme.png')
send(DISCONNECT_MESSAGE)
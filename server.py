import socket
import threading

ADDR = (socket.gethostbyname(socket.gethostname()),5050)
FORMAT = 'utf-8'
HEADER = 64 
DISCONNECT_MESSAGE = '!DISCONNECT'

# AF_INET -> IPV4, SOCK_STREAM -> TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    file = open('new.png','wb')
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            if msg == bytes(DISCONNECT_MESSAGE, encoding=FORMAT):
                connected = False
            file.write(msg)
            conn.send("Send succesfull".encode(FORMAT))
            
    print(f"[LEFT]{addr} left the server.")
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR[0]}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start()

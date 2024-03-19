import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server Started. Listening:")
conn, addr = server.accept()


while True:
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            conn.send("Connection Terminated.".encode(FORMAT))
            conn.close()
            break
        else:
            salary = 0
            if int(msg) <= 40:
                salary = int(msg) * 200
            else:
                salary = 8000 + (int(msg) - 40) * 300
            print(f'Salary = {salary}')
            conn.send(f'Salary = {salary}'.encode(FORMAT))

conn.send("Connection Terminated.".encode(FORMAT))
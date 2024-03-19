import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)
FORMAT="utf8"
DISCONNECT="END"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(message):
    message = message.encode(FORMAT)
    message_length=len(message)
    send_length=str(message_length).encode(FORMAT)
    send_length+= b' ' * (HEADER-len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    i=input("Hours : ")
    if i == DISCONNECT:
        send(DISCONNECT)
        break
    else:
        send(i)
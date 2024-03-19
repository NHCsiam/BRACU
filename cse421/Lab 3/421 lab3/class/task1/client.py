import socket

HEADER=16
PORT= 5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE='END'

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send_message(message):
    message=message.encode(FORMAT)
    message_length=len(message)
    send_length=str(message_length).encode(FORMAT)
    send_length+= b' ' * (HEADER-len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send_message(f'Client\'s IP: {SERVER} and Device Name: {socket.gethostname()}')
send_message(DISCONNECT_MESSAGE)
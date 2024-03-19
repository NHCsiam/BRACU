import socket

HEADER=16
PORT= 5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE='END'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


server.listen()
print("Server Started. Listening:")


conn,addr=server.accept()

while True:
    message_length=conn.recv(HEADER).decode(FORMAT)
    if message_length:
        message_length=int(message_length)
        message=conn.recv(message_length).decode(FORMAT)
        if message ==DISCONNECT_MESSAGE:
            conn.send("Connection Terminated.".encode(FORMAT))
            conn.close()
            break
        else:
            count = 0
            vowel = "aeiouAEIOU"
            for i in message:
                if i in vowel:
                    count+=1
            if count==0:
                conn.send("Not enough vowels".encode(FORMAT))
            elif count <=2:
                conn.send("Enough Vowels I guess".encode(FORMAT))
            else:
                conn.send("Too Many Vowels".encode(FORMAT))

            conn.send("Connection Terminated.".encode(FORMAT))
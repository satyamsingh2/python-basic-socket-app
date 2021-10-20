import socket
from threading import Thread


name = input("input your name: ")

IP = "localhost"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP,PORT))

client.send(name.encode())

def send(client):
    while True:
        data = f"{name}: {input('')}"
        client.send(data.encode())

def recieve(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except:
            print("closing client")
            client.close()
            break


thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=recieve, args=(client,))
thread2.start()

import socket
import threading

ip = "127.0.0.1"
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))
server.listen(5)

print('* Server listening')

def handle_client(client_sock):
    request = client_sock.recv(1024)

    print("Request: %s" % (request))

    client_sock.send("Ack!")

    client_sock.close()

while True:
    client, addr = server.accept()

    print("* Accepted a connection")

    client_handler = threading.Thread(target=handle_client, args=(client))
    client_handler.start()

import socket

target_host = "www.google.ie"
target_port = 80

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send data
client.send(b'GET / HTTP/1.1\r\nHost: google.ie\r\n\r\n')

# Receive data
response = client.recv(4096)

print(response)

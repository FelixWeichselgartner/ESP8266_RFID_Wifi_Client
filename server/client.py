import socket

HOST, PORT = "127.0.0.1", 9999
#HOST, PORT = "192.168.178.77", 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
#client.send(b"uid: 0b d0 17 1c\n")
client.send(b"uid: 0b d0 17 1c\n")
response = client.recv(4096)
print(response)

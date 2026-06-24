import socket

PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('', PORT))

print("Listening for messages...")

while True:
    data, addr = client.recvfrom(1024)

    print(f"\nMessage from {addr[0]}")
    print(data.decode())
import socket

PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("Broadcast Server Started")

while True:
    message = input("Enter Message: ")

    server.sendto(
        message.encode(),
        ('255.255.255.255', PORT)
    )

    print("Message Sent")
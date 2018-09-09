import socket
import sys

# Creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST: localhost, PORT: 10000
server_address = ('localhost', 10000)
# Print that you're about to start a socket connection
connection = ["HOST", server_address[0], "PORT",server_address[1]]
print('[SYN] Starting Client Connection to Server:', connection)

# Build connection to the server
s.connect(server_address)

choice = "y"
while choice == "y":
    try:
        message = input("Input message to send to the server: ")
        # Sends message as a byte string
        s.sendall(message.encode('utf-8'))

        amount_received = 0
        amount_expected = len(message)

        while amount_expected > amount_received:
            data = s.recv(1024)
            amount_received += len(data)
            print("[ACK] Recevived data from server: %s" % data)
    finally:
        print("Closing socket connection..")

    try:
        choice = input("Would you like to send more data? Enter[y/N]: ")
        if choice == "N":
            break
    except:
        pass
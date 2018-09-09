import socket
from logging import log

# Creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST: localhost, PORT: 10000
server_address = ('localhost', 10000)
# Print that you're about to start a socket connection
connection = ['HOST', server_address[0], 'PORT', server_address[1]]
print('[SYN] Starting Server Connection:', connection)

# Bind the host and port number to the socket
s.bind(server_address)
s.listen(5)

while True:
    conn, addr = s.accept() # Returns host address and port
    try:
        if addr:
            print('[ACK] Received connection from:', addr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = conn.recv(1024)
            if data:
                print('[ACK] Received:', data, '\nSending data back to the client\n')
                # Send the data back to the client with all uppercase
                conn.sendall(data.upper())
            else:
                print('No more data received from:', addr)
                conn.close()

    except OSError as e:
        # Clean up the connection
        conn.close
        print('ERROR:', log(2, e),'\n[FIN] Connection Closed')
        exit()
import socket

listen_ip = "127.0.0.1" # listen on localhost
listen_port = 9999 # to avoid giving sudo

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket IPv4 TCP
server.bind((listen_ip, listen_port)) # associate socket to ip and port
server.listen() # socket passively listening

print(f"listening on {listen_ip}:{listen_port}... (ctrl+c to cancel)") # status msg

while True: # loop in order to keep server active
    connection, address = server.accept() # wait for incoming connection and return tuple
    with connection:
        print(f"connected from {address}") # logs who connects
        while True:
            data = connection.recv(1024) # returns max 1024 bytes
            if not data: # empty bytes means client disconnected
                break
            connection.sendall(data) # echo data back until fully sent

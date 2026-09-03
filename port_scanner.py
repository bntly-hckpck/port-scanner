import socket

target_ip = "127.0.0.1" # localhost ip
target_port = 9999 # same as listen port of server

# create socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 TCP

# attempt connection
result = my_socket.connect_ex((target_ip, target_port))

if result == 0: # 0 = success, connected
    print(f"port {target_port} open on {target_ip}")
else: # anything else = errno code
    print(f"port {target_port} closed or unreachable (error: {result})")

my_socket.close() # release socket

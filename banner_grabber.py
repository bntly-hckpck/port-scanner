import socket

def banner_grabbing(target_ip, port): # connect to single open port and try to read banner

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 TCP, new socket
    result = my_socket.connect_ex((target_ip, port)) # attempt connection
    if result != 0:
        my_socket.close()
        return None

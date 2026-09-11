import socket

def banner_grabbing(target_ip, port): # connect to single open port and try to read banner

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 TCP, new socket
    result = my_socket.connect_ex((target_ip, port)) # attempt connection

    if result != 0:
        my_socket.close()
        return None

    my_socket.settimeout(3)

    try:
        recv_bytes = my_socket.recv(1024) # read up to 1024 bytes
        banner = recv_bytes.decode("utf-8", errors="ignore").strip() # bytes to string
        if banner == "":
            banner = None
    
    except socket.timeout: # connection accepted but remained silent  
        banner = None
    
    my_socket.close() # always release socket
    return banner

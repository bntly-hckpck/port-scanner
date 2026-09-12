import socket

def port_scanning(target_ip, start_port, end_port):

    open_ports = [] # collects open ports to return to caller

    for port in range(start_port, end_port + 1): # +1 to not exclude last port
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 TCP, new socket per iteration
        result = my_socket.connect_ex((target_ip, port)) # attempt connection

        if result == 0:
            print(f"port {port} open on {target_ip}")
            open_ports.append(port) # append port to open_ports[]

        my_socket.close() # always release socket
    
    return open_ports   

if __name__ == "__main__":
    open_ports = port_scanning("127.0.0.1", 9990, 9999) # choose port range here
    print(f"open ports found: {open_ports}") # display open ports, [] if none

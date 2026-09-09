import socket

def port_scanning(target_ip, start_port, end_port):

    open_ports = []

    for port in range(start_port, end_port + 1):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = my_socket.connect_ex((target_ip, port))

        if result == 0:
            print(f"port {port} open on {target_ip}")
            open_ports.append(port)

        my_socket.close()
    
    return open_ports   
    

import socket

def test_server1(): # banner testing, speaks first serving every client
    host = "127.0.0.1"
    port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 TCP
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port can be reused after server shutdown
    server.bind((host, port)) # bind to localhost

    server.listen(3) # start listening, queue max 3 requests
    print("test server running on 127.0.0.1:9999...")

    while True:
        conn, addr = server.accept() # accept connection
        conn.send(b"[testbanner]\n") # send test banner
        conn.close() # close connection

if __name__ == "__main__":
    test_server1()

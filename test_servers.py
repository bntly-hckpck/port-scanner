import socket
import threading # added threading

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

def test_server2(): # silent testing, accepts and never speaks
    host = "127.0.0.1"
    port = 9998

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))

    server.listen(3)
    print("test server running on 127.0.0.1:9998...")
    
    while True:
        conn, addr = server.accept()

if __name__ == "__main__":
    # threading as both servers have blocking loops
    thread1 = threading.Thread(target=test_server1) # run in parallel
    thread2 = threading.Thread(target=test_server2)
    thread1.start()
    thread2.start()

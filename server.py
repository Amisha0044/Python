# to achieve socket programming in Python, we need to import a module "socket"
import socket

# server socket - to accept the connections; socket(IPv4/IPv6, TCP/UDP) creates a socket; in args: 1) is the network IPv4 or IPv6, 2) is the network used TCP or UDP (by default it takes IPv4 and TCP if not mentioned explicitely)
s = socket.socket()
print("socket created")

# binding the socket with the port number along with the IP address of server
s.bind(('localhost',9999))    # server IP, port - bind takes both these things as single argument

# start listening to the clients, wait for client to connect, how many clients to connect at one time? - allowing buffer for 3 connections
s.listen(3)
print("waiting for connections...")

while True:
    # to accept the connection from client; accept() gives you 2 things- client socket and client IP address
    c, addr = s.accept()

    # receive the data from client
    name = c.recv(1024).decode()

    print('connected with ', addr, name)      # connected with  ('127.0.0.1', 51386) -- localhost and port number(port num is self generated) of client

    # send data to client
    # c.send('Welcome to Telusko')      # TypeError: a bytes-like object is required, not 'str'
    c.send(bytes("Welcome to Telusko", "utf-8")) # TypeError: string argument without an encoding


    # once work is done, close the connection
    c.close()

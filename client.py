import socket

# creating client socket
c = socket.socket()

# binding to port number along with IP is the job of server, not of client, client simpley connect and send data

# connect to server, mention IP of server and port as single argument
c.connect(('localhost',9999))

# receive the data being sent out by the server to the client

# sending the name of client user to the server
# send() is used to send data between two sockets
name = input("enter your name: ")
# c.send(bytes(name,'utf-8'))
# or
c.send(name.encode('utf-8'))

# recv(bufferSize)
data_from_server = c.recv(1024)
print(data_from_server)             # b'Welcome to Telusko' -- indicates this is in bytes
print(data_from_server.decode())    # Welcome to Telusko

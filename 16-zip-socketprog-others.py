#####################################################
# zip() FUNCTION
# - like a zip of jeans/pants - connect multiple components(list,tuple,set,dict)
#
#
# SOCKET PROGRAMMING
# - Used for client-server, client-client(peer-to-pier) communication
#
# - Socket:
#   * A socket is a software construct that allows programs to communicate with each other over a network. It's an endpoint for sending and receiving data.
#   * A socket is one endpoint of a two way communication link between two programs running on the network.
# - Socket Programming:
#   * Socket programming in Python involves using the socket module to establish communication between two programs (clients and servers) over a network.
#   * It's a fundamental way to create network applications, allowing data exchange between applications, even those running on different machines.
#
# - For socket programming, we need 2 things- port and protocol:
#   * TCP (Transmission Control Protocol): connection-oriented network - first create a connection, and then communicate i.e. send packets
#     UDP (User Datagram Protocol): connection-less network - no need to have a connection, simply send packets but only drawback is we don't know if packets reached there or not as no connection.ts;
#   * Port - we also need a port for communicating over internet; this port should not be already getting used by any global service or by any service you are running on that port.
#
#####################################################


# zip() FUNCTION

names = ('navin','kiran','harsh','navin')
comp = ('dell','apple','MS','oracle')

zipped = zip(names, comp)
print(zipped)           # <zip object at 0x000001A0F1B3FD40>

# for (a,b) in zipped:
#     print(a,b)
# navin dell
# kiran apple
# harsh MS
# navin oracle

# zipped_list = list(zipped)
# print(zipped_list)      # [('navin', 'dell'), ('kiran', 'apple'), ('harsh', 'MS'), ('navin', 'oracle')]
# zipped_tuple = tuple(zipped)
# print(zipped_tuple)     # (('navin', 'dell'), ('kiran', 'apple'), ('harsh', 'MS'), ('navin', 'oracle'))
# zipped_set = set(zipped)
# print(zipped_set)       # {('navin', 'oracle'), ('harsh', 'MS'), ('navin', 'dell'), ('kiran', 'apple')}
zipped_dict = dict(zipped)
print(zipped_dict)      # {'navin': 'oracle', 'kiran': 'apple', 'harsh': 'MS'}



# SOCKET PROGRAMMING


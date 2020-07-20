This program is primarily used as a socket hosting server which allows a user to transfer data over an open socket server.

Note: There is no encryption method/protective measure so be wary from sending any sensitive data. This program was primarily used to data recorded by simple lab devices over a network.


## UPDATES
# February 9, 2018 (changes)

1) added a server resfresh method to zmq_client_socket
2) created live plotting
3) added logging

# February 10, 2018 

1) uploaded new version onto github.
2) decreased printing rate
3) Discovered that liveplotting and printing values continuously was eating up ram. Caused the computer to crash after 10 hours.
	(about 2 GBS of ram gets used up after passing this for 22 hours).
